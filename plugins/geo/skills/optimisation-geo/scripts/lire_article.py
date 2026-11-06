#!/usr/bin/env python3
"""Récupère un article et le convertit en Markdown, sans reformuler le texte.

Usage :
  python3 lire_article.py <url ou fichier.html> [-o article.md]

Le Markdown sort sur la sortie standard (ou dans le fichier demandé). Les
informations de la page (titre, dates) sortent sur la sortie d'erreur.

Codes de sortie : 0 réussi, 3 page illisible ou texte trop court.

Bibliothèque standard uniquement. Do Ingenia, licence MIT (voir LICENSE-CODE).
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

VIDES = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
         "meta", "param", "source", "track", "wbr"}
A_RETIRER = {"script", "style", "noscript", "svg", "nav", "aside", "footer",
             "form", "button", "iframe", "template", "select", "figcaption"}
CLASSES_A_RETIRER = re.compile(
    r"(^|[\s_-])(breadcrumbs?|fil-ariane|share|sharing|partage|related|similaires?"
    r"|sidebar|newsletter|comments?|commentaires?|toc|sommaire|table-of-contents"
    r"|author-box|navigation|pagination|cookies?)($|[\s_-])", re.I)
FIN_ARTICLE = re.compile(
    r"^#{1,6} \W*(articles? similaires?|articles? liés?|à lire aussi|lire aussi"
    r"|sur le même sujet|dans la même catégorie)\W*$", re.I)
CONTENEURS = {"div", "section", "ul", "ol", "dl", "header"}
TITRES = {"h1", "h2", "h3", "h4", "h5", "h6"}
BLOCS = TITRES | {"p", "ul", "ol", "table", "blockquote", "pre", "div", "section",
                  "article", "main", "header", "details", "figure", "dl"}


class Noeud:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs or []), parent
        self.enfants = []

    def texte(self):
        return "".join(e if isinstance(e, str) else e.texte() for e in self.enfants)

    def tous(self):
        for e in self.enfants:
            if isinstance(e, Noeud):
                yield e
                yield from e.tous()


class Analyseur(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.racine = Noeud("document")
        self.courant = self.racine

    def handle_starttag(self, tag, attrs):
        n = Noeud(tag, attrs, self.courant)
        self.courant.enfants.append(n)
        if tag not in VIDES:
            self.courant = n

    def handle_endtag(self, tag):
        n = self.courant
        while n is not self.racine and n.tag != tag:
            n = n.parent
        if n is not self.racine:
            self.courant = n.parent

    def handle_data(self, data):
        self.courant.enfants.append(data)


def retirer_balises(n):
    n.enfants = [e for e in n.enfants
                 if not (isinstance(e, Noeud) and e.tag in A_RETIRER)]
    for e in n.enfants:
        if isinstance(e, Noeud):
            retirer_balises(e)


def nettoyer(n, total):
    """Retire la navigation, les encarts et ce qui n'est pas l'article.

    Une classe suspecte ne retire un élément que s'il pèse peu dans la page :
    un conteneur nommé « with-sidebar » peut contenir tout l'article.
    """
    garde = []
    for e in n.enfants:
        if isinstance(e, Noeud):
            classes = " ".join([e.attrs.get("class") or "", e.attrs.get("id") or ""])
            # Jamais sur un titre ou un paragraphe : l'id d'un titre reprend souvent son
            # texte, et « PBN : comment ça fonctionne ? » n'est pas un bloc de commentaires.
            if e.tag in CONTENEURS and CLASSES_A_RETIRER.search(classes) \
                    and len(e.texte().split()) < 0.3 * total:
                continue
            if e.tag == "header" and not any(x.tag == "h1" for x in e.tous()):
                continue
            # Une grille de cartes d'articles : plusieurs <article> dans un même bloc.
            if sum(1 for x in e.tous() if x.tag == "article") >= 3 \
                    and len(e.texte().split()) < 0.5 * total:
                continue
            nettoyer(e, total)
        garde.append(e)
    n.enfants = garde


def mots_de_texte(n):
    """Les mots des paragraphes, listes et tableaux, liens exclus."""
    total = 0
    for x in n.tous():
        if x.tag in ("p", "li", "td", "th", "blockquote"):
            total += len(x.texte().split())
            total -= sum(len(a.texte().split()) for a in x.tous() if a.tag == "a")
    return total


def choisir_article(racine):
    """Le plus petit élément qui contient l'essentiel du texte de la page.

    Les cartes d'articles similaires portent souvent la balise <article> : la
    balise ne suffit donc pas à désigner le contenu principal.
    """
    corps = next((n for n in racine.tous() if n.tag == "body"), racine)
    retirer_balises(corps)  # les scripts fausseraient le décompte des mots
    nettoyer(corps, len(corps.texte().split()))
    total = mots_de_texte(corps)
    courant = corps
    while total:
        suivant = next((e for e in courant.enfants if isinstance(e, Noeud)
                        and mots_de_texte(e) >= 0.85 * total), None)
        if suivant is None:
            break
        courant = suivant
    return courant


def espaces(t):
    return re.sub(r"[ \t\r\n\f]+", " ", t)


def en_ligne(n, base):
    """Le texte d'un bloc, avec gras, italique, code et liens."""
    sortie = ""
    for e in n.enfants:
        if isinstance(e, str):
            sortie += espaces(e)
            continue
        if e.tag == "br":
            sortie += " "
        elif e.tag == "img":
            continue
        elif e.tag in ("strong", "b", "em", "i", "code"):
            brut = en_ligne(e, base)
            marque = {"strong": "**", "b": "**", "em": "*", "i": "*", "code": "`"}[e.tag]
            coeur = brut.strip()
            if coeur:
                debut = " " if brut[:1].isspace() else ""
                fin = " " if brut[-1:].isspace() else ""
                sortie += f"{debut}{marque}{coeur}{marque}{fin}"
            else:
                sortie += brut
        elif e.tag == "a":
            brut = en_ligne(e, base)
            href = (e.attrs.get("href") or "").strip()
            coeur = brut.strip()
            if coeur and href and not href.startswith(("#", "javascript:")):
                debut = " " if brut[:1].isspace() else ""
                fin = " " if brut[-1:].isspace() else ""
                sortie += f"{debut}[{coeur}]({urljoin(base, href)}){fin}"
            else:
                sortie += brut
        else:
            sortie += en_ligne(e, base)
    return sortie


def rendre_table(n, base):
    lignes = []
    for tr in (x for x in n.tous() if x.tag == "tr"):
        cellules = [en_ligne(c, base).strip().replace("|", "\\|")
                    for c in tr.enfants if isinstance(c, Noeud) and c.tag in ("td", "th")]
        if cellules:
            lignes.append(cellules)
    if not lignes:
        return []
    largeur = max(len(l) for l in lignes)
    lignes = [l + [""] * (largeur - len(l)) for l in lignes]
    rendu = ["| " + " | ".join(lignes[0]) + " |", "|" + "---|" * largeur]
    rendu += ["| " + " | ".join(l) + " |" for l in lignes[1:]]
    return ["\n".join(rendu)]


def rendre_liste(n, base, retrait=0):
    lignes = []
    for i, li in enumerate((c for c in n.enfants
                            if isinstance(c, Noeud) and c.tag == "li"), 1):
        marque = f"{i}." if n.tag == "ol" else "-"
        copie = Noeud("li")
        sous = []
        for c in li.enfants:
            if isinstance(c, Noeud) and c.tag in ("ul", "ol"):
                sous.append(c)
            else:
                copie.enfants.append(c)
        lignes.append(" " * retrait + f"{marque} " + en_ligne(copie, base).strip())
        for s in sous:
            lignes.extend(rendre_liste(s, base, retrait + 2))
    return lignes


def rendre(n, base):
    blocs, tampon = [], []

    def vider():
        if tampon:
            t = "".join(tampon).strip()
            if t:
                blocs.append(t)
            tampon.clear()

    for e in n.enfants:
        if isinstance(e, str):
            tampon.append(espaces(e))
            continue
        if e.tag not in BLOCS and not any(x.tag in BLOCS for x in e.tous()):
            enveloppe = Noeud("span")
            enveloppe.enfants.append(e)
            tampon.append(en_ligne(enveloppe, base))
            continue
        vider()
        if e.tag in TITRES:
            t = en_ligne(e, base).strip()
            if t:
                blocs.append("#" * int(e.tag[1]) + " " + t)
        elif e.tag == "p":
            t = en_ligne(e, base).strip()
            if t:
                blocs.append(t)
        elif e.tag in ("ul", "ol"):
            lignes = rendre_liste(e, base)
            if lignes:
                blocs.append("\n".join(lignes))
        elif e.tag == "table":
            blocs.extend(rendre_table(e, base))
        elif e.tag == "blockquote":
            for b in rendre(e, base):
                blocs.append("\n".join("> " + l for l in b.split("\n")))
        elif e.tag == "pre":
            blocs.append("```\n" + e.texte().strip("\n") + "\n```")
        elif e.tag == "hr":
            continue
        else:
            blocs.extend(rendre(e, base))
    vider()
    return blocs


def meta(racine):
    infos = {"titre_page": "", "date_publication": "", "date_modification": ""}
    for n in racine.tous():
        if n.tag == "title" and not infos["titre_page"]:
            infos["titre_page"] = espaces(n.texte()).strip()
        elif n.tag == "meta":
            nom = n.attrs.get("property") or n.attrs.get("name") or ""
            val = n.attrs.get("content") or ""
            if nom == "article:published_time" and not infos["date_publication"]:
                infos["date_publication"] = val
            elif nom == "article:modified_time" and not infos["date_modification"]:
                infos["date_modification"] = val
        elif n.tag == "script" and "ld+json" in (n.attrs.get("type") or ""):
            brut = n.texte()
            try:
                json.loads(brut)
            except ValueError:
                continue
            m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', brut)
            if m and not infos["date_publication"]:
                infos["date_publication"] = m.group(1)
            m = re.search(r'"dateModified"\s*:\s*"([^"]+)"', brut)
            if m and not infos["date_modification"]:
                infos["date_modification"] = m.group(1)
    return infos


def recuperer(source):
    if not re.match(r"https?://", source):
        with open(source, encoding="utf-8", errors="replace") as f:
            return f.read(), ""
    req = urllib.request.Request(source, headers={
        "User-Agent": "Mozilla/5.0 (compatible; optimisation-geo)",
        "Accept-Language": "fr,en;q=0.5"})
    with urllib.request.urlopen(req, timeout=30) as r:
        jeu = r.headers.get_content_charset() or "utf-8"
        return r.read().decode(jeu, errors="replace"), r.geturl()


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("source")
    p.add_argument("-o", "--sortie")
    a = p.parse_args()
    try:
        html, base = recuperer(a.source)
    except (urllib.error.URLError, OSError, ValueError) as e:
        print(f"Page illisible : {e}", file=sys.stderr)
        return 3

    analyseur = Analyseur()
    analyseur.feed(html)
    racine = analyseur.racine
    infos = meta(racine)
    h1_page = next((espaces(en_ligne(n, base)).strip() for n in racine.tous()
                    if n.tag == "h1"), "")
    titres_page = [espaces(n.texte()).strip() for n in racine.tous()
                   if n.tag in ("h1", "h2", "h3") and n.texte().strip()]
    article = choisir_article(racine)
    blocs = rendre(article, base)
    for i, b in enumerate(blocs):
        if FIN_ARTICLE.match(b):
            blocs = blocs[:i]
            break
    if h1_page and not any(b.startswith("# ") for b in blocs):
        blocs.insert(0, "# " + h1_page)
    texte = "\n\n".join(blocs) + "\n"

    for cle, val in infos.items():
        print(f"{cle} : {val or 'non trouvé'}", file=sys.stderr)
    def comparable(t):
        return espaces(re.sub(r"[*`\[]", "", t).replace("\u00a0", " "))

    plat = comparable(re.sub(r"\]\([^)]*\)", "", texte))
    absents = [t for t in titres_page if comparable(t) not in plat]
    if absents:
        print("titres_non_repris (à vérifier) :", file=sys.stderr)
        for t in absents:
            print(f"  - {t}", file=sys.stderr)
    mots = len(texte.split())
    print(f"mots : {mots}", file=sys.stderr)
    if mots < 100:
        print("Texte trop court : page chargée par JavaScript ou protégée ? "
              "Demander à l'utilisateur de coller l'article.", file=sys.stderr)
        return 3
    if a.sortie:
        with open(a.sortie, "w", encoding="utf-8") as f:
            f.write(texte)
    else:
        sys.stdout.write(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
