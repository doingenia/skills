#!/usr/bin/env python3
"""Contrôle un article après ajouts : hors surlignage, rien n'a changé.

Usage :
  python3 controle_ajouts.py <original.md> <avec-ajouts.md> [--plafond 20]
  python3 controle_ajouts.py --releve <article.md>

Le contrôle échoue si, une fois retirés les ajouts surlignés ==…== :
  - une phrase d'origine a changé, disparu ou bougé (accents et apostrophes compris) ;
  - un titre a changé, disparu ou bougé, ou un titre non surligné est apparu ;
  - un texte non surligné est apparu, ou un paragraphe a été coupé ;
  - un surlignage se trouve au milieu d'une phrase d'origine ;
  - les ajouts dépassent le plafond (20 % des mots de l'article) ;
  - un ajout contient un nombre absent de l'article.

Seuls les espaces (insécables compris) et les retours à la ligne à l'intérieur
d'un paragraphe sont ignorés.

Codes de sortie : 0 réussi, 1 échec, 2 contrôle impossible.

Bibliothèque standard uniquement. Do Ingenia, licence MIT (voir LICENSE-CODE).
"""
import argparse
import datetime
import difflib
import re
import sys
import unicodedata

SURLIGNE = r"==(?=\S)(?:(?!==).)*?(?<=\S)=="
RE_SURLIGNE = re.compile(SURLIGNE)
RE_TOUT_SURLIGNE = re.compile(r"^==(?=\S)(?:(?!==).)*(?<=\S)==$")
RE_TITRE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$")
RE_LISTE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_SEPARATEUR = re.compile(r"^\|?[\s:|-]*-[\s:|-]*\|?$")
ABREVIATIONS = {"m", "mm", "mme", "mlle", "dr", "pr", "me", "st", "ste", "cf",
                "ex", "p", "pp", "art", "av", "vol", "éd", "n", "no", "fig",
                "env", "etc", "réf", "chap", "j.-c", "c.-à-d", "s.a", "inc"}
MAJUSCULE = "A-ZÀ-ÖØ-ÞŒ"


def normaliser(texte):
    """Forme composée des accents, espaces unifiés, rien d'autre."""
    t = unicodedata.normalize("NFC", texte).replace("\r\n", "\n").replace("\r", "\n")
    t = re.sub(r"[​‌‍﻿]", "", t)
    return re.sub(r"[      \t]", " ", t)


def separer_entete(texte):
    """Sépare un en-tête YAML éventuel, qui doit rester identique."""
    m = re.match(r"---\n.*?\n---\n", texte, re.S)
    return (m.group(0), texte[m.end():]) if m else ("", texte)


def retirer_surlignage(s):
    return s.replace("==", "")


def cellules(ligne):
    coeur = ligne.strip().strip("|")
    return [c.strip() for c in re.split(r"(?<!\\)\|", coeur)]


def est_ajout(ligne):
    """Vrai si la ligne entière est un ajout surligné, et le type d'ajout."""
    s = ligne.strip()
    m = RE_TITRE.match(s)
    if m and RE_TOUT_SURLIGNE.match(m.group(2)):
        return "titre"
    if s.startswith("|") and s.endswith("|") and not RE_SEPARATEUR.match(s):
        cs = [c for c in cellules(s) if c]
        if cs and all(RE_TOUT_SURLIGNE.match(c) for c in cs):
            return "tableau"
        return None
    sans_puce = RE_LISTE.sub("", s, count=1)
    if RE_TOUT_SURLIGNE.match(sans_puce):
        return "texte"
    return None


def extraire_ajouts(lignes):
    """Sépare les lignes conservées des ajouts surlignés."""
    gardees, ajouts, dans_code, prec_tableau = [], [], False, False
    for ligne in lignes:
        s = ligne.strip()
        if s.startswith("```") or s.startswith("~~~"):
            dans_code = not dans_code
        if dans_code or s.startswith("```") or s.startswith("~~~"):
            gardees.append(ligne)
            prec_tableau = False
            continue
        if prec_tableau and RE_SEPARATEUR.match(s) and s:
            prec_tableau = False
            continue
        genre = est_ajout(ligne)
        if genre:
            ajouts.append((genre, s))
            prec_tableau = genre == "tableau"
            gardees.append("")
        else:
            gardees.append(ligne)
            prec_tableau = False
    return gardees, ajouts


def genre_ligne(s):
    if RE_TITRE.match(s):
        return "titre"
    if s.startswith("|"):
        return "tableau"
    if s.startswith(">"):
        return "citation"
    if RE_LISTE.match(s):
        return "liste"
    return "para"


def en_blocs(lignes):
    """La structure du texte : suites de lignes de même nature."""
    blocs, courant, genre, dans_code = [], [], None, False

    def fermer():
        nonlocal courant, genre
        if courant:
            joint = " ".join(courant) if genre == "para" else "\n".join(courant)
            blocs.append((genre, joint))
        courant, genre = [], None

    for ligne in lignes:
        s = ligne.strip()
        if s.startswith("```") or s.startswith("~~~"):
            if not dans_code:
                fermer()
                genre = "code"
            courant.append(ligne.rstrip())
            dans_code = not dans_code
            if not dans_code:
                fermer()
            continue
        if dans_code:
            courant.append(ligne.rstrip())
            continue
        if not s:
            fermer()
            continue
        g = genre_ligne(s)
        if g == "titre":
            fermer()
            m = RE_TITRE.match(s)
            blocs.append(("titre", m.group(1) + " " + re.sub(r" +", " ", m.group(2))))
            continue
        if g != genre:
            fermer()
            genre = g
        retrait = ligne[:len(ligne) - len(ligne.lstrip())] if g == "liste" else ""
        courant.append(retrait + re.sub(r" +", " ", s))
    fermer()
    return blocs


def phrases(texte):
    """Découpe en phrases, adaptée au français (guillemets, majuscules accentuées)."""
    t = re.sub(r"\s+", " ", texte).strip()
    if not t:
        return []
    motif = re.compile(
        r"[.!?…]+(?:\s*[»”\")\]*_]+)*\s+(?=[«“\"(\[*_]*\s*[" + MAJUSCULE + r"0-9])")
    resultat, debut = [], 0
    for m in motif.finditer(t):
        avant = t[debut:m.start()].split(" ")[-1].lower().strip("(«“\"*_")
        if t[m.start()] == "." and (avant in ABREVIATIONS or (len(avant) == 1 and avant.isalpha())):
            continue
        resultat.append(t[debut:m.end()].strip())
        debut = m.end()
    if debut < len(t):
        resultat.append(t[debut:].strip())
    return resultat


def unites(blocs):
    sortie = []
    for genre, contenu in blocs:
        if genre == "para":
            sortie.extend(phrases(contenu))
        elif genre == "liste" or genre == "citation":
            for ligne in contenu.split("\n"):
                sortie.extend(phrases(ligne))
        elif genre == "tableau":
            sortie.extend(contenu.split("\n"))
        elif genre != "titre":
            sortie.append(contenu)
    return sortie


def ecart_mots(a, b):
    """Les premiers mots qui diffèrent, pour montrer le changement."""
    ma, mb = a.split(), b.split()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ma, mb, autojunk=False).get_opcodes():
        if op != "equal":
            return f"« {' '.join(ma[i1:i2]) or '∅'} » → « {' '.join(mb[j1:j2]) or '∅'} »"
    return "différence de mise en forme"


def tronque(s, n=130):
    return s if len(s) <= n else s[:n - 1] + "…"


def comparer_phrases(a, b):
    """Décrit, phrase par phrase, ce qui a changé."""
    pbs = []
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        ga, gb = list(a[i1:i2]), list(b[j1:j2])
        for s in list(ga):
            if s in gb:
                ga.remove(s)
                gb.remove(s)
                pbs.append(f"DÉPLACÉE : {tronque(s)}")
            elif s in b and s not in a[:i1] + a[i2:]:
                ga.remove(s)
                pbs.append(f"DÉPLACÉE : {tronque(s)}")
        for s in ga:
            proche = max(gb, key=lambda x: difflib.SequenceMatcher(None, s, x, autojunk=False).ratio(),
                         default=None)
            if proche and difflib.SequenceMatcher(None, s, proche, autojunk=False).ratio() >= 0.5:
                gb.remove(proche)
                pbs.append(f"MODIFIÉE : {tronque(s)}\n      changement : {ecart_mots(s, proche)}")
            else:
                pbs.append(f"SUPPRIMÉE : {tronque(s)}")
        for s in gb:
            if s not in a:
                pbs.append(f"AJOUTÉE SANS SURLIGNAGE : {tronque(s)}")
    return pbs


def compter_mots(texte):
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", texte)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"(?m)^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", " ", t)
    t = t.replace("==", " ")
    return len(re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", t))


def nombres(texte):
    t = re.sub(r"\]\([^)]*\)", "]", texte)
    t = re.sub(r"https?://\S+", " ", t)
    return {re.sub(r"\s", "", m).replace(",", ".")
            for m in re.findall(r"\d(?:[\d.,]| (?=\d{3}\b))*\d|\d", t)}


def noms_propres(texte):
    """Mots à majuscule en milieu de phrase."""
    t = texte.replace("==", "").replace("**", "")
    t = re.sub(r"(?m)^[#|\s-]+", "", t).replace("|", ". ")
    noms = set()
    for ph in (p for ligne in t.split("\n") for p in phrases(ligne)):
        for mot in re.findall(r"(?<=[\s(«])[" + MAJUSCULE + r"][\w’'-]+", ph):
            noms.add(mot)
    return noms


def controle(chemin_o, chemin_r, plafond):
    try:
        with open(chemin_o, encoding="utf-8") as f:
            origine = normaliser(f.read())
        with open(chemin_r, encoding="utf-8") as f:
            revu = normaliser(f.read())
    except (OSError, UnicodeDecodeError) as e:
        print(f"CONTRÔLE IMPOSSIBLE : {e}")
        return 2

    en_tete_o, corps_o = separer_entete(origine)
    en_tete_r, corps_r = separer_entete(revu)
    if not corps_o.strip():
        print("CONTRÔLE IMPOSSIBLE : l'original est vide.")
        return 2
    lignes_o = corps_o.split("\n")
    hors_code = re.sub(r"(?ms)^(```|~~~).*?^\1\s*$", "", corps_o)
    if RE_SURLIGNE.search(hors_code):
        print("CONTRÔLE IMPOSSIBLE : l'original contient déjà du texte entre == et ==. "
              "Impossible de distinguer les ajouts. Retirer ces marques de la copie de "
              "référence, puis relancer.")
        return 2

    gardees, ajouts = extraire_ajouts(corps_r.split("\n"))
    blocs_o, blocs_r = en_blocs(lignes_o), en_blocs(gardees)
    echecs = []

    if en_tete_o != en_tete_r:
        echecs.append("En-tête YAML modifié.")

    titres_o = [c for g, c in blocs_o if g == "titre"]
    titres_r = [c for g, c in blocs_r if g == "titre"]
    print("TITRES")
    if titres_o == titres_r:
        print(f"  identiques ({len(titres_o)})")
    else:
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(
                None, titres_o, titres_r, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            for t in titres_o[i1:i2]:
                echecs.append(f"Titre modifié ou supprimé : {t}")
                print(f"  ÉCHEC, modifié ou supprimé : {t}")
            for t in titres_r[j1:j2]:
                echecs.append(f"Titre nouveau non surligné, ou déplacé : {t}")
                print(f"  ÉCHEC, nouveau non surligné, ou déplacé : {t}")
    for genre, ligne in ajouts:
        if genre == "titre" and ligne.startswith("# "):
            echecs.append(f"Un ajout ne peut pas être un titre de niveau 1 : {ligne}")
            print(f"  ÉCHEC, ajout de niveau 1 : {ligne}")

    print("PHRASES D'ORIGINE")
    u_o, u_r = unites(blocs_o), unites(blocs_r)
    pbs_phrases = comparer_phrases(u_o, u_r)
    interieurs = [l for g, c in blocs_r if g != "code"
                  for l in c.split("\n") if RE_SURLIGNE.search(l)]
    for l in interieurs:
        pbs_phrases.append(f"SURLIGNAGE DANS UNE PHRASE D'ORIGINE : {tronque(l)}")
    blocs_sans_titres = [b for b in blocs_o if b[0] != "titre"], [b for b in blocs_r if b[0] != "titre"]
    if blocs_o != blocs_r and not pbs_phrases and titres_o == titres_r:
        if blocs_sans_titres[0] != blocs_sans_titres[1]:
            pbs_phrases.append("PARAGRAPHE OU LISTE COUPÉ OU FUSIONNÉ : les phrases sont intactes, "
                               "mais un ajout a été placé à l'intérieur d'un bloc.")
        else:
            pbs_phrases.append("ORDRE MODIFIÉ entre un titre et le texte qui le suit.")
    if pbs_phrases:
        for p in pbs_phrases:
            print(f"  ÉCHEC, {p}")
        echecs.extend(pbs_phrases)
    else:
        print(f"  {len(u_o)} phrases et lignes, toutes identiques, dans le même ordre")

    print("AJOUTS")
    texte_ajouts = "\n".join(l for _, l in ajouts)
    mots_o = compter_mots(corps_o)
    mots_a = compter_mots(texte_ajouts)
    part = 100 * mots_a / mots_o if mots_o else 0
    print(f"  {len(ajouts)} lignes surlignées, {mots_a} mots pour {mots_o} mots d'origine ({part:.1f} %)")
    if part > plafond:
        echecs.append(f"Ajouts au-delà du plafond : {part:.1f} % pour {plafond:g} %.")
        print(f"  ÉCHEC, plafond de {plafond:g} % dépassé")
    inconnus = sorted(nombres(texte_ajouts) - nombres(corps_o))
    if inconnus:
        echecs.append("Nombres absents de l'article : " + ", ".join(inconnus))
        print("  ÉCHEC, nombres absents de l'article : " + ", ".join(inconnus))
    bas_o = corps_o.lower()
    noms = sorted(n for n in noms_propres(texte_ajouts) if n.lower() not in bas_o)
    if noms:
        print("  À VÉRIFIER, mots à majuscule absents de l'article : " + ", ".join(noms))

    print()
    if echecs:
        print(f"RÉSULTAT : ÉCHEC ({len(echecs)} problème(s)). Ne pas livrer comme réussi.")
        return 1
    print("RÉSULTAT : RÉUSSI. Hors ajouts surlignés, l'article est identique mot pour mot.")
    return 0


def releve(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            texte = normaliser(f.read())
    except (OSError, UnicodeDecodeError) as e:
        print(f"LECTURE IMPOSSIBLE : {e}")
        return 2
    _, corps = separer_entete(texte)
    blocs = en_blocs(corps.split("\n"))
    print(f"mots : {compter_mots(corps)}")
    titres = [c for g, c in blocs if g == "titre"]
    h1 = [t[2:] for t in titres if t.startswith("# ")]
    print("h1 : " + (" | ".join(h1) if h1 else "absent"))
    if h1:
        print(f"h1_question : {'oui' if h1[0].rstrip().endswith('?') else 'non'}")
        print(f"h1_caracteres : {len(h1[0])}")
    h2 = [t[3:] for t in titres if t.startswith("## ")]
    q = [t for t in h2 if t.rstrip().endswith("?")]
    print(f"h2 : {len(h2)}, dont {len(q)} en question")
    for t in h2:
        print(f"  - {t}")
    premiers = " ".join(c for g, c in blocs if g != "titre")[:900]
    print("resume_annonce : " + ("oui" if re.search(
        r"(?i)\b(en bref|en résumé|en resume|résumé|l['’]essentiel|à retenir|tl;?dr)\b", premiers[:400]) else "non"))
    print("debut : " + tronque(premiers, 700))
    tableaux = [c for g, c in blocs if g == "tableau"]
    avec_entete = sum(1 for t in tableaux if len(t.split("\n")) > 1
                      and RE_SEPARATEUR.match(t.split("\n")[1]))
    print(f"tableaux : {len(tableaux)}, dont {avec_entete} avec ligne d'en-tête")
    print(f"listes : {sum(1 for g, _ in blocs if g == 'liste')}")
    faq = [t for t in titres if re.search(r"(?i)\bfaq\b|questions? fréquentes?|foire aux questions", t)]
    print("faq : " + (" | ".join(faq) if faq else "non repérée"))
    if faq:
        i = titres.index(faq[0])
        niveau = len(faq[0].split(" ")[0])
        sous = []
        for t in titres[i + 1:]:
            if len(t.split(" ")[0]) <= niveau:
                break
            sous.append(t)
        print(f"faq_questions_en_titre : {len(sous)}")
    liens = re.findall(r"\]\((https?://[^)\s]+)", corps)
    domaines = sorted({re.sub(r"^https?://(www\.)?", "", l).split("/")[0] for l in liens})
    print(f"liens : {len(liens)}, domaines : {', '.join(domaines) or 'aucun'}")
    annee = datetime.date.today().year
    annees = {}
    for g, c in blocs:
        sans_liens = re.sub(r"\]\([^)]*\)", "]", c)
        for a in re.findall(r"\b(19[5-9]\d|20[0-4]\d)\b", sans_liens):
            if int(a) < annee:
                annees.setdefault(a, tronque(sans_liens, 110))
    print(f"annee_en_cours : {annee}")
    print("annees_passees : " + (str(len(annees)) if annees else "aucune"))
    for a in sorted(annees):
        print(f"  - {a} : {annees[a]}")
    print("debuts_de_section_a_relire :")
    trouve = False
    for i, (g, c) in enumerate(blocs[:-1]):
        if g == "titre" and blocs[i + 1][0] != "titre":
            suite = blocs[i + 1][1]
            suite = re.sub(r"^[>*_\s-]+", "", suite)
            if re.match(r"(?i)(il|ils|elle|elles|cela|ça|ceci|ce|cet|cette|ces|celui-ci|celle-ci|ceux-ci|celles-ci|leur|leurs)\b", suite):
                trouve = True
                print(f"  - {c} : {tronque(suite, 110)}")
    if not trouve:
        print("  aucun")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("fichiers", nargs="*")
    p.add_argument("--plafond", type=float, default=20)
    p.add_argument("--releve", metavar="ARTICLE")
    a = p.parse_args()
    if a.releve:
        return releve(a.releve)
    if len(a.fichiers) != 2:
        p.print_usage()
        return 2
    return controle(a.fichiers[0], a.fichiers[1], a.plafond)


if __name__ == "__main__":
    sys.exit(main())
