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

Trois séries de passages, le même jour (11/11/2026), dans ces conditions :

- **Essai 1** : version interne de `/humaniser`, dont cette version publique est tirée, et texte 1
  avec sa ligne de date. Les trois skills. Pangram mesuré.
- **Essai 2** : première version publique de `/humaniser`, et texte 1 sans la ligne de date. Les
  trois skills. Pangram non mesuré.
- **Essai 3** : `/humaniser` seul, version publique 0.1.0 telle qu'elle est dans ce dépôt (sans ce
  dossier d'essais). Elle corrige deux défauts vus à l'essai 2 : la cible de rythme acceptait une
  baisse sous le rythme de l'original, et le contrôle des faits ignorait les nombres écrits en
  lettres. Pangram non mesuré.

## Les résultats

Un passage par skill, par texte et par essai. Faits relevés en aveugle ; rythme en coefficient de
variation (cible de `/humaniser` : au moins 60 %, et pas moins que l'original) ; coût moyen par
texte relevé par Claude Code.

| Passage | Faits, texte 1 | Faits, texte 2 | Rythme, texte 1 | Rythme, texte 2 | Coût |
|---|---|---|---|---|---|
| Originaux | | | 52 % | 64 % | |
| `/humaniser`, essai 1 (interne) | 1 nuance adoucie | fidèle | 68 % | 66 % | 0,28 $ |
| `/humaniser`, essai 2 (avant correction) | 3 éléments perdus (« trois niveaux », deux phrases d'annonce) | 1 nuance adoucie | 72 % | 60 % | 0,20 $ |
| `/humaniser`, essai 3 (0.1.0) | 1 nuance adoucie | fidèle | 65 % | 66 % | 0,25 $ |
| blader/humanizer, essai 1 | 2 nuances, 1 ajout | 1 nuance | 54 % | 47 % | 0,13 $ |
| blader/humanizer, essai 2 | 1 ajout, 1 nuance | fidèle | 51 % | 64 % | 0,13 $ |
| samber humaniseur-fr, essai 1 | 3 ajouts | titre et 7 intertitres changés, 6 ajouts, 1 fait déformé | 55 % | 59 % | 0,17 $ |
| samber humaniseur-fr, essai 2 | 3 ajouts, 1 nuance, 1 liste mise en prose | 2 ajouts, 1 fait déformé, 2 nuances, 3 listes mises en prose | 59 % | 67 % | 0,17 $ |

Pour lire le rythme : les textes humains de l'étude de référence sont à 78 %, ceux de ChatGPT à
50 % (voir [`references/etudes.md`](../references/etudes.md)).

**Pangram** (essai 1 seulement) : les huit textes, originaux compris, sont jugés écrits par une IA
à 100 %.

Exemples d'écarts relevés :
- samber, texte 2, essai 1 : « éviter quelques pièges classiques » devient « éviter deux ou trois
  pièges qui reviennent chaque année », alors que le texte en liste cinq.
- samber, texte 2, essai 2 : « deux démarches distinctes » devient « n'ont rien à voir l'une avec
  l'autre », alors que le même chiffre d'affaires sert aux deux.
- `/humaniser`, texte 1, essai 2 : « On distingue trois niveaux de chantier » devient « Les
  chantiers se rangent en niveaux » ; le nombre disparaît. À l'essai 3, après correction, il reste.

Les réécritures sont dans [`resultats/`](resultats/) : `t<texte>-humaniser.md` pour l'essai 3,
`t<texte>-<skill>-essai2.md` pour les trois skills à l'essai 2.

## Dans Mistral Vibe

Un passage de `/humaniser` 0.1.0 dans Mistral Vibe 3.1.2, avec le modèle GLM-5.3 hébergé par
Mistral, sur le texte 2, avec la même consigne. La skill a été copiée dans `~/.vibe/skills/` et
appelée par `/humaniser` ; chaque commande a été approuvée à la main.

- **Rythme** : 64 → 69 %. Le premier brouillon était à 64,2 %, juste au niveau de l'original : la
  skill a repris deux paragraphes, comme le prévoit sa règle.
- **Faits** (relecture en aveugle, même protocole) : un élément perdu. La phrase « Premier point à
  clarifier : votre déclaration à l'Urssaf et votre déclaration d'impôts sont deux démarches
  distinctes » a été supprimée ; l'intertitre et la liste qui suivent le disent encore, mais plus
  explicitement. Aucun ajout, aucune nuance changée, structure intacte.
- **Coût** : non relevé.

La réécriture est dans [`resultats/t2-humaniser-vibe.md`](resultats/t2-humaniser-vibe.md). Un seul
passage, sur un seul texte : il montre que la skill fonctionne dans Vibe, pas qu'elle y donne les
mêmes résultats qu'avec Claude.

## Ce que ces chiffres disent, et ne disent pas

- **Peu de passages, de petits écarts.** Deux textes, un passage par skill et par essai : on ne peut
  pas conclure sur un écart d'une nuance ou de quelques points de rythme. Les chiffres varient d'un
  passage à l'autre pour la même skill (de 65 à 72 % sur le texte 1 pour `/humaniser`, de 47 à 64 %
  sur le texte 2 pour blader).
- **Ce qui se répète** : `/humaniser` garde la structure et n'ajoute aucun fait, à chacun de ses six
  passages ; il donne le rythme le plus varié trois fois sur quatre dans les essais à trois skills.
  samber ajoute des affirmations à chaque passage et touche à la structure. blader garde la
  structure, et sa fidélité est proche de celle de `/humaniser`.
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
