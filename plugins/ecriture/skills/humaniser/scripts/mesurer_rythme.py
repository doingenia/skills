#!/usr/bin/env python3
"""Mesure le rythme d'un texte : dispersion de la longueur des phrases.

Repères tirés de Labbé, Labbé et Savoy (2024), vœux des présidents français contre ChatGPT
(voir references/etudes.md) : même longueur moyenne (21 mots), mais un texte humain disperse bien plus ses
phrases. Coefficient de variation 78 % contre 50 %, rapport 9e décile / 1er décile 3,8 contre 1,9,
et mode < médiane < moyenne, alors que chez ChatGPT les trois sont presque égaux.

Seule la prose compte : frontmatter, intertitres, listes, tableaux, citations en bloc et lignes
courtes sans ponctuation finale (titres d'un texte collé) sont écartés.

Usage :
    python3 mesurer_rythme.py texte.md               # un texte
    python3 mesurer_rythme.py avant.md apres.md      # avant et après réécriture
    python3 mesurer_rythme.py texte.md --json
"""
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

# Repères de l'étude (tableau 10), pour lire les chiffres.
REPERES = {
    "humain": {"cv": 78.1, "d9_d1": 3.8},
    "chatgpt": {"cv": 50.3, "d9_d1": 1.9},
}
COURTE = 12  # une phrase de moins de 12 mots compte comme courte
LONGUE = 39  # au-delà de 39 mots, l'étude ne voit presque plus de phrases de ChatGPT

FIN_DE_PHRASE = re.compile(r"(?<=[.!?…])[»”\"')\]]*\s+(?=[«“\"(\[]?[A-ZÀ-ÖØ-Þ0-9])")
MOT = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+(?:[-’'][0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+)*")


def prose(texte: str) -> list[str]:
    """Paragraphes de prose, sans frontmatter ni éléments de structure."""
    if texte.startswith("---"):
        fin = texte.find("\n---", 3)
        if fin != -1:
            texte = texte[fin + 4:]
    texte = re.sub(r"<!--.*?-->", "", texte, flags=re.S)
    paragraphes = []
    for ligne in texte.splitlines():
        l = ligne.strip()
        if not l or l.startswith(("#", "|", ">", "- ", "* ", "+ ")) or re.match(r"^\d+[.)] ", l):
            continue
        l = re.sub(r"\*\*|__|==|`", "", l)
        l = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", l)
        # Ligne courte sans ponctuation finale : un titre ou une cellule de texte collé.
        if not re.search(r"[.!?…:»”\"]$", l) and len(MOT.findall(l)) < 15:
            continue
        paragraphes.append(l)
    return paragraphes


def phrases(paragraphes: list[str]) -> list[int]:
    longueurs = []
    for p in paragraphes:
        for ph in FIN_DE_PHRASE.split(p):
            n = len(MOT.findall(ph))
            if n:
                longueurs.append(n)
    return longueurs


def decile(valeurs: list[int], q: float) -> float:
    v = sorted(valeurs)
    pos = q * (len(v) - 1)
    bas = int(pos)
    haut = min(bas + 1, len(v) - 1)
    return v[bas] + (v[haut] - v[bas]) * (pos - bas)


def mesurer(chemin: str) -> dict:
    longueurs = phrases(prose(Path(chemin).read_text(encoding="utf-8")))
    if len(longueurs) < 2:
        return {"fichier": chemin, "phrases": len(longueurs), "erreur": "trop peu de phrases pour mesurer"}
    moyenne = statistics.mean(longueurs)
    ecart = statistics.stdev(longueurs)
    d1, d9 = decile(longueurs, 0.1), decile(longueurs, 0.9)
    compte = Counter(longueurs)
    mode = max(compte, key=lambda k: (compte[k], -k))
    n = len(longueurs)
    return {
        "fichier": chemin,
        "phrases": n,
        "moyenne": round(moyenne, 1),
        "mediane": statistics.median(longueurs),
        "mode": mode,
        "ecart_type": round(ecart, 1),
        "cv": round(100 * ecart / moyenne, 1),
        "d1": round(d1, 1),
        "d9": round(d9, 1),
        "d9_d1": round(d9 / d1, 2) if d1 else None,
        "courtes_pct": round(100 * sum(1 for x in longueurs if x < COURTE) / n, 1),
        "longues_pct": round(100 * sum(1 for x in longueurs if x > LONGUE) / n, 1),
        "mode_mediane_moyenne_croissants": mode < statistics.median(longueurs) < moyenne,
        "longueurs": longueurs,
    }


def lecture(m: dict) -> str:
    if "erreur" in m:
        return f"{m['fichier']} : {m['erreur']} ({m['phrases']})."
    h, g = REPERES["humain"], REPERES["chatgpt"]
    ordre = "oui" if m["mode_mediane_moyenne_croissants"] else "non"
    return (
        f"{m['fichier']}\n"
        f"  {m['phrases']} phrases, moyenne {m['moyenne']} mots (médiane {m['mediane']}, mode {m['mode']})\n"
        f"  coefficient de variation {m['cv']} %   (humain {h['cv']} %, ChatGPT {g['cv']} %)\n"
        f"  rapport D9/D1 {m['d9_d1']}   (humain {h['d9_d1']}, ChatGPT {g['d9_d1']})\n"
        f"  phrases de moins de {COURTE} mots : {m['courtes_pct']} % ; de plus de {LONGUE} mots : {m['longues_pct']} %\n"
        f"  mode < médiane < moyenne : {ordre}"
    )


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    mesures = [mesurer(a) for a in args]
    if "--json" in sys.argv:
        print(json.dumps(mesures, ensure_ascii=False, indent=1))
    else:
        print("\n\n".join(lecture(m) for m in mesures))
        if min(m["phrases"] for m in mesures) < 20:
            print("\nMoins de 20 phrases : chiffres indicatifs.")


if __name__ == "__main__":
    main()
