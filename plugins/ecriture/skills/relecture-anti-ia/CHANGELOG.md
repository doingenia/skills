# relecture-anti-ia : journal des versions

## 0.2.2

- Lancé sans texte ni fichier, le skill affiche l'aide et demande le texte au lieu de reprendre un texte précédent.
- Version corrigée toujours dans un bloc de code Markdown dans la conversation.
- Indication d'arguments pour la commande `/doingenia-ecriture:relecture-anti-ia`, et usage documenté.

## 0.2.1

- Commande d'aide : « relecture-anti-ia aide » affiche les options.
- Mode d'emploi `README.md` dans le dossier du skill.

## 0.2.0

- Nouvelle règle 10 : pas de fausse opposition (« ce n'est pas X, c'est Y »), ni dans le texte relu ni dans la réécriture.
- Nouvelle règle 17 : pas d'affirmation orpheline, sans preuve.
- Nouveau garde-fou 6 : le mot-clé principal reste dans le titre et dans l'ouverture.
- Relevé systématique des incohérences internes (nombres annoncés, dates, noms), signalées sans être tranchées.
- Sortie dans un fichier Markdown `<nom>.relecture.md` quand un fichier est fourni, ou sur demande « en fichier ».
- Version corrigée rendue dans un bloc de code Markdown dans la conversation, pour une copie propre.
- Règles renumérotées (18 au total) ; le test ChatGPT devient la règle 18.

## 0.1.0

- Première version : 16 règles, garde-fous contre l'invention de faits, sortie en trois parties (diagnostic, version corrigée, matière à fournir), mode « diagnostic seul ».
