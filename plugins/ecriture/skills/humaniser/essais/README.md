# Jeu d'essais : `/humaniser` face à blader et samber

Deux textes écrits par une IA, réécrits par trois skills d'humanisation, pour que chacun puisse
rejouer la comparaison et vérifier nos chiffres.

## Les textes

| Fichier | Sujet | Mots |
|---|---|---|
| [`textes/texte1-salle-de-bains.md`](textes/texte1-salle-de-bains.md) | Prix d'une rénovation de salle de bains et choix de l'artisan | 854 |
| [`textes/texte2-auto-entrepreneur.md`](textes/texte2-auto-entrepreneur.md) | Première déclaration de revenus d'un auto-entrepreneur | 904 |

Les deux ont été générés pour l'essai, sur des sujets grand public, hors de tout travail pour un
client. Ils sont publiés tels qu'ils ont été passés aux skills, y compris leur mise en forme de texte
copié (intertitres et tableaux sans balises Markdown). Une seule modification : la ligne de date et
d'auteur, sous le titre du texte 1, a été retirée avant l'essai 2, pour qu'aucune donnée personnelle
ne figure dans le jeu de test.

## Le protocole

- **Skills comparées** : `/humaniser` (Do Ingenia), [blader/humanizer](https://github.com/blader/humanizer)
  v4.0.0 et [samber/cc-skills](https://github.com/samber/cc-skills) `humaniseur-fr` v1.1.3.
- **Même modèle** pour toutes : Claude Sonnet 5.5, dans Claude Code en mode non interactif.
- **Sessions isolées** : un dossier neuf par passage, avec la seule skill testée et le texte, sans
  configuration ni mémoire partagée.
- **Même consigne**, sans fichier de voix :

  ```
  /<skill> "texte.md" Registre : courant, article de blog grand public. Écris la version finale dans le fichier texte-humanise.md, à côté du texte.
  ```

- **Outils permis** : lecture, écriture, recherche dans les fichiers, et `python3` (pour le script
  de rythme de `/humaniser`).
- **Faits** : chaque réécriture a été comparée à l'original par un agent Claude lancé dans un
  contexte vierge, qui ignorait quelle skill l'avait produite : les copies étaient anonymisées
  (versions X, Y et Z tirées au hasard, frontmatter retiré).
- **Rythme** : coefficient de variation de la longueur des phrases, mesuré par
  [`scripts/mesurer_rythme.py`](../scripts/mesurer_rythme.py) sur toutes les versions.

Deux essais, le même jour (11/11/2026), dans ces conditions :

- **Essai 1** : version interne de `/humaniser`, dont cette version publique est tirée, et texte 1
  avec sa ligne de date. Pangram mesuré.
- **Essai 2** : version publique 0.1.0 de `/humaniser`, telle qu'elle est dans ce dépôt (sans ce
  dossier d'essais), et texte 1 sans la ligne de date. Pangram non mesuré.

## Les résultats

**Faits** (relecture en aveugle) :

| | Texte 1, essai 1 | Texte 1, essai 2 | Texte 2, essai 1 | Texte 2, essai 2 |
|---|---|---|---|---|
| `/humaniser` | 1 nuance adoucie | 3 éléments perdus (le nombre « trois niveaux », deux phrases d'annonce) | fidèle | 1 nuance adoucie |
| blader/humanizer | 2 nuances, 1 ajout | 1 ajout, 1 nuance | 1 nuance | fidèle |
| samber humaniseur-fr | 3 ajouts | 3 ajouts, 1 nuance, 1 liste mise en prose | titre et 7 intertitres changés, 6 ajouts, 1 fait déformé | 2 ajouts, 1 fait déformé, 2 nuances, 3 listes mises en prose |

**Rythme** (coefficient de variation ; cible de `/humaniser` : 60 %) :

| | Texte 1, essai 1 | Texte 1, essai 2 | Texte 2, essai 1 | Texte 2, essai 2 |
|---|---|---|---|---|
| Original | 52 % | 52 % | 64 % | 64 % |
| `/humaniser` | **68 %** | **72 %** | **66 %** | 60 % |
| blader/humanizer | 54 % | 51 % | 47 % | 64 % |
| samber humaniseur-fr | 55 % | 59 % | 59 % | **67 %** |

Pour lire ces chiffres : les textes humains de l'étude de référence sont à 78 %, ceux de ChatGPT à
50 % (voir [`references/etudes.md`](../references/etudes.md)).

**Coût moyen par texte**, relevé par Claude Code sur chaque session :

| | Essai 1 | Essai 2 |
|---|---|---|
| `/humaniser` | 0,28 $ | 0,20 $ |
| blader/humanizer | 0,13 $ | 0,13 $ |
| samber humaniseur-fr | 0,17 $ | 0,17 $ |

**Pangram** (essai 1 seulement) : les huit textes, originaux compris, sont jugés écrits par une IA
à 100 %.

Exemples d'écarts relevés :
- samber, texte 2, essai 1 : « éviter quelques pièges classiques » devient « éviter deux ou trois
  pièges qui reviennent chaque année », alors que le texte en liste cinq.
- samber, texte 2, essai 2 : « deux démarches distinctes » devient « n'ont rien à voir l'une avec
  l'autre », alors que le même chiffre d'affaires sert aux deux.
- `/humaniser`, texte 1, essai 2 : « On distingue trois niveaux de chantier » devient « Les
  chantiers se rangent en niveaux » ; le nombre disparaît.

Les six réécritures de l'essai 2 sont dans [`resultats/`](resultats/), nommées
`t<texte>-<skill>.md`.

## Ce que ces chiffres disent, et ne disent pas

- **Ce qui se répète d'un essai à l'autre** : samber ajoute des affirmations à chaque passage et
  touche à la structure ; `/humaniser` et blader gardent la structure ; `/humaniser` atteint la cible
  de rythme aux quatre passages (de justesse au dernier, 60,1 %) et donne la plus forte dispersion
  trois fois sur quatre. À l'essai 2, sur le texte 2, blader et samber l'atteignent aussi.
- **Ce qui varie** : la fidélité de `/humaniser` et de blader est proche, et leur classement
  s'inverse d'un essai à l'autre. Sur le texte 2 de l'essai 2, `/humaniser` fait baisser le rythme
  (64 → 60 %) : la cible est atteinte, mais l'original était déjà au-dessus.
- **Deux textes, deux essais, c'est peu.** Un autre tirage du modèle donnerait d'autres chiffres.
  Le comparatif montre des tendances, pas une mesure stable.
- **Deux sujets du même genre** : des articles de conseil grand public, sans fichier de voix. Rien ne
  dit ce que donnent les trois skills sur un texte technique, littéraire ou réglementé, ni avec un
  texte de référence, qui est l'usage prévu de `--voix`.
- **Aucune des trois ne trompe Pangram**, et `/humaniser` ne le cherche pas. Pangram annonce repérer
  98,8 % des textes passés par un humaniseur ; un texte réécrit à la main par une rédactrice, dans un
  autre essai, était jugé humain à 100 %.

## Rejouer l'essai

1. Créez un dossier vide par passage, copiez-y un des deux textes sous le nom `texte.md`, et la
   skill à tester dans `.claude/skills/<nom>/`.
2. Lancez, depuis ce dossier :

   ```
   claude -p '/humaniser "texte.md" Registre : courant, article de blog grand public. Écris la version finale dans le fichier texte-humanise.md, à côté du texte.' \
     --model claude-sonnet-5-5 --allowedTools "Read,Write,Edit,Glob,Grep,Bash(python3:*)" --output-format json > resultat.json
   ```

   Remplacez `/humaniser` par `/humanizer` ou `/humaniseur-fr` pour les deux autres. Le coût de la
   session est dans le champ `total_cost_usd` de `resultat.json`.
3. Mesurez le rythme de l'original et de la réécriture :

   ```
   python3 ../scripts/mesurer_rythme.py texte.md texte-humanise.md
   ```

4. Pour les faits, donnez l'original et les réécritures, renommées au hasard, à un relecteur (une
   personne, ou un agent dans un contexte vierge) qui ne sait pas laquelle vient de quelle skill, et
   demandez-lui la liste des faits perdus, ajoutés, déformés ou nuancés autrement, et des changements
   de structure.
