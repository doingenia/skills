#!/usr/bin/env bash
# Vérifie, avant chaque commit, qu'aucun fichier préparé ne contient un terme
# de la liste interdite (noms de clients, noms de personnes interviewées).
#
# La liste vit hors du dépôt, un terme par ligne, dans :
#   $DOINGENIA_LISTE_INTERDITE, ou par défaut ~/.config/doingenia/liste-interdite.txt
#
# Usage : lancé automatiquement par pre-commit, ou à la main :
#   scripts/verifier-liste-interdite.sh

set -euo pipefail

LISTE="${DOINGENIA_LISTE_INTERDITE:-$HOME/.config/doingenia/liste-interdite.txt}"

if [ ! -s "$LISTE" ]; then
  echo "Liste interdite introuvable ou vide : $LISTE" >&2
  echo "Commit bloqué par précaution. Créez la liste avant de continuer." >&2
  exit 1
fi

# En local, on affiche les lignes trouvées : la sortie reste sur votre machine.
if git grep --cached -n -i -w -F -f "$LISTE" -- . ; then
  echo "" >&2
  echo "Commit bloqué : les lignes ci-dessus contiennent un terme de la liste interdite." >&2
  exit 1
fi

exit 0
