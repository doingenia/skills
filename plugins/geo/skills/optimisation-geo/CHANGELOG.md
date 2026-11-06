# optimisation-geo : journal des versions

## 0.1.0

- Première version : relevé de la forme d'un article français (URL, fichier ou texte collé).
- Ajouts surlignés, seulement s'ils manquent et si le contenu s'y prête : résumé `**En bref**`, tableau tiré des données de l'article, FAQ de questions réelles.
- Propositions non appliquées : titre, H2 en question, sources à trouver.
- Signalements sans réécriture : passages vagues, sections qui ne se comprennent pas seules, page ancienne selon l'intention, années dépassées.
- Script `controle_ajouts.py` : hors surlignage, phrases et titres identiques mot pour mot, ajouts limités à 20 % des mots, aucun nombre absent de l'article.
- Script `lire_article.py` : conversion d'une page en Markdown sans reformulation.
- Testé avec Claude Code (URL, fichier) et dans Mistral Vibe (fichier).
