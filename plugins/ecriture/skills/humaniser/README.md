# humaniser

**Humaniser un texte français écrit par une IA, sans changer ce qu'il dit.** Donnez un article, une page ou une newsletter rédigés par une IA : le skill en réécrit la prose pour qu'elle se lise comme celle d'un humain qui connaît son sujet. Il est fait pour ne perdre ni inventer aucun fait, et contrôle chacun ; le titre, les intertitres, les tableaux et la FAQ restent en place, et un script mesure le rythme des phrases avant et après.

Il ne promet pas de passer les détecteurs. Dans le premier essai de notre comparatif, les huit textes, originaux compris, sont jugés écrits par une IA à 100 % par Pangram, quelle que soit la skill qui les a réécrits.

## Un exemple

Un paragraphe fictif, écrit pour montrer le geste (le premier de [references/exemples.md](references/exemples.md)). Les réécritures réelles des essais sont dans [essais/resultats/](essais/resultats/).

**5 phrases → 3 · 86 mots → 30 · 5 faits et 1 nuance gardés**

Légende : ~~barré~~ = supprimé · **gras** = fait gardé · *italique* = nuance gardée · (1) à (4) = changements expliqués dessous.

**Avant**

> (1) ~~Dans un contexte de hausse des prix de l'énergie, le choix d'un mode de chauffage constitue un enjeu crucial pour de nombreux ménages.~~ La pompe à chaleur air-eau (2) ~~se positionne comme une solution particulièrement intéressante, offrant~~ un **rendement élevé** tout en permettant de **réduire significativement la facture**. (3) ~~Il ne s'agit pas simplement d'un équipement, mais d'un véritable investissement pour l'avenir.~~ Son coût, compris **entre 10 000 et 16 000 €** **pose comprise**, *peut toutefois sembler élevé*. C'est pourquoi il est essentiel de bien **se renseigner sur les aides disponibles**.

**Après**

> (4) Une pompe à chaleur air-eau coûte **de 10 000 à 16 000 €**, **pose comprise**, ce qui *peut sembler élevé*. Son **rendement élevé réduit nettement la facture**. **Renseignez-vous** d'abord **sur les aides disponibles**.

1. Ouverture de décor et « enjeu crucial » : la phrase ne dit rien sur la pompe à chaleur.
2. « Se positionne comme » et « offrant » : des tournures de modèle qui retardent le fait.
3. Fausse opposition « pas un équipement, mais un investissement » : personne ne croyait l'inverse.
4. Le prix passe en tête, avec « pose comprise ».

Ce qui ne change pas : la nuance « peut sembler élevé » ne devient pas « c'est cher », et le skill n'ajoute pas que les aides couvrent une partie du prix, ni quand les demander, puisque le texte d'origine ne le dit pas.

## Installation

Dans Claude Code :

```
/plugin marketplace add doingenia/skills
/plugin install doingenia-ecriture@doingenia-skills
```

Ou, avec tout outil compatible avec les Agent Skills :

```
npx skills add doingenia/skills
```

Dans Mistral Vibe, copiez ce dossier dans `~/.vibe/skills/` (voir le [README du dépôt](../../../../README.md#installation)), puis relancez Vibe.

Dans Claude.ai ou l'application Claude : téléchargez [humaniser.zip](https://github.com/doingenia/skills/releases/download/humaniser-v0.1.2/humaniser.zip) (version 0.1.2, sans le dossier d'essais), puis importez-le dans Réglages, section Skills. Activez l'exécution de code et la création de fichiers (Réglages, Capacités), sinon le rythme ne peut pas être mesuré.

Aucune clé d'API ni compte n'est nécessaire. Le script de mesure du rythme est en Python, sans dépendance : il faut un outil qui peut lancer Python et écrire des fichiers. Sans cela, le skill réécrit quand même le texte et dit que le rythme n'a pas été mesuré.

Testé avec Claude Code (Claude Sonnet 5.5) sur les deux textes du comparatif, et sur le texte 2 dans Claude.ai (Claude Opus 5.5) et dans Mistral Vibe 3.1.2 (modèle GLM-5.3 hébergé par Mistral) : voir [essais/](essais/README.md#dans-claudeai-et-mistral-vibe).

## Utilisation

Le skill ne se déclenche pas tout seul : lancer `/humaniser`, c'est décider d'humaniser (voir « Les choix »). Dans Claude Code, tapez `/humaniser` et laissez l'autocomplétion faire le reste :

```
/doingenia-ecriture:humaniser "brouillons/article.md"
/doingenia-ecriture:humaniser "brouillons/article.md" --voix "references/page-a-propos.md"
```

Dans Mistral Vibe, la commande est `/humaniser` :

```
/humaniser "brouillons/article.md" --voix "references/page-a-propos.md"
```

Dans Claude.ai, tapez `/humaniser` et joignez le fichier **au même message** : sans texte ni pièce jointe, le skill s'arrête et vous le demande.

Ou lancez-le sans argument et collez le texte dans le même message.

| Élément | Effet |
|---|---|
| le texte (chemin ou texte collé) | Obligatoire. 150 mots au moins. |
| `--voix "fichier"` | Facultatif. Un guide de rédaction (registre, mots imposés ou interdits, précautions) ou, mieux, un texte humain de référence : une page de votre site, un article que vous avez écrit, une lettre. Le skill en reprend la longueur des phrases, les liaisons, le vocabulaire et la ponctuation, et vise la même dispersion des phrases. |

Sans `--voix`, le skill propose une fois d'en fournir un, puis travaille avec le texte seul.

Le fichier de voix est le levier le plus sûr : une étude sur le français montre qu'avec un court texte humain en exemple, ChatGPT imite assez bien un style. C'est aussi la seule source d'où le skill peut tirer un fait concret pour remplacer une généralité.

## Ce que vous obtenez

1. **La version réécrite**, dans un nouveau fichier `<nom>-humanise.md` à côté du texte, avec la date de la passe dans le frontmatter. Votre fichier n'est jamais modifié. Un texte collé est rendu dans la réponse.
2. **Un compte rendu court** :
   - le rythme avant et après, mesuré par le script (coefficient de variation, rapport entre phrases longues et courtes) ;
   - les tournures corrigées, par famille et avec un nombre, et la raison de chaque correction ;
   - le tableau de contrôle des faits : chaque chiffre, prix, durée, nom, nuance, et la phrase finale qui le porte ;
   - les passages qui manquent de matière, avec la question à vous poser pour les remplir ;
   - ce qui a été laissé exprès (citation, précaution, structure), et les coquilles relevées, non corrigées.

## Ce qui le distingue

Nous avons comparé `/humaniser` aux deux skills d'humanisation les plus proches, [blader/humanizer](https://github.com/blader/humanizer) et [samber/cc-skills `humaniseur-fr`](https://github.com/samber/cc-skills), sur deux textes neufs, avec le même modèle, en sessions isolées, et une relecture des faits par un agent Claude en contexte vierge, sur des copies anonymisées, sans savoir quelle skill avait produit quelle version. Le protocole complet et les textes sont dans [essais/](essais/README.md).

Résultats de la version de ce dépôt (0.1.0, essai 3) et des deux autres skills (essai 2) :

| | Faits, texte 1 | Faits, texte 2 | Rythme, texte 1 | Rythme, texte 2 | Coût moyen par texte |
|---|---|---|---|---|---|
| Originaux | | | 52 % | 64 % | |
| `/humaniser` | 1 nuance adoucie | fidèle | 65 % | 66 % | 0,25 $ |
| blader/humanizer | 1 ajout, 1 nuance | fidèle | 51 % | 64 % | 0,13 $ |
| samber humaniseur-fr | 3 ajouts, 1 nuance, 1 liste mise en prose | 2 ajouts, 1 fait déformé, 2 nuances, 3 listes mises en prose | 59 % | 67 % | 0,17 $ |

Le rythme est le coefficient de variation de la longueur des phrases ; la cible du skill est d'au moins 60 %, et jamais moins que l'original.

Deux textes et un passage par skill et par essai ne permettent pas de conclure sur de petits écarts : les chiffres varient d'un passage à l'autre pour une même skill. Les trois essais, leurs écarts et leurs limites sont détaillés dans [essais/](essais/README.md). Ce qui se répète d'un essai à l'autre :

- **Il garde la structure et n'ajoute aucun fait**, à chacun de ses six passages. samber, lui, ajoute des affirmations à chaque passage : il a transformé « quelques pièges » en « deux ou trois pièges » face à une liste de cinq, et « deux démarches distinctes » en « n'ont rien à voir l'une avec l'autre ». blader garde la structure, avec une fidélité proche.
- **Il donne le rythme le plus varié trois fois sur quatre** dans les essais à trois skills, et atteint sa cible à chaque passage. Le seul passage où il faisait baisser le rythme de l'original (64 → 60 %, essai 2) a conduit à corriger la cible.
- **Il mesure au lieu d'estimer.** Un script calcule la dispersion des phrases avant et après, et le skill reprend les paragraphes trop réguliers tant que la cible n'est pas atteinte, ou dit pourquoi.
- **Il contrôle chaque fait par ce à quoi il se rapporte**, pas seulement par sa présence : un prix réécrit ne doit pas se lire comme une durée, « avant tout » ne devient jamais « seul », et un nombre écrit en lettres compte comme un chiffre. Ce dernier point vient d'un essai où « trois niveaux » avait disparu.
- **Il ne touche pas à la structure** qui sert le référencement et la citation par les IA : titre, intertitres en question, tableaux, FAQ. blader autorise à changer la structure ; samber retire les blocs de FAQ, transforme en prose les tableaux qu'il juge superflus et compte les intertitres en question parmi les marques d'IA.
- **Il garde les précautions des secteurs réglementés** (santé, santé animale, finance, droit, fiscalité) et celles qu'impose votre guide. Il ne retire qu'une précaution empilée sur une autre. blader ne protège que les mentions légales et de sécurité ; samber réduit les précautions sans exception de secteur.
- **Il n'invente rien.** Un détail ajouté vient de votre fichier de voix, et le compte rendu dit d'où ; sinon, le skill signale le manque et la question à poser.

**Ses limites** : il coûte plus cher (0,25 $ par texte d'environ 850 mots avec Claude Sonnet 5.5, contre 0,13 $ pour blader et 0,17 $ pour samber), parce qu'il mesure, contrôle et reprend. Et il n'a été essayé que sur deux articles de conseil grand public, sans fichier de voix.

## Les choix

- **Une méthode française**, appuyée sur la seule étude chiffrée que nous ayons trouvée sur le style d'une IA en français (Labbé, Labbé et Savoy, 2024).
- **Pas de détection de l'origine du texte.** Lancer le skill, c'est décider d'humaniser. Dans nos essais, un comptage de tournures ne distinguait pas un texte humain d'un texte d'IA, et les études françaises sur la détection vont dans le même sens.
- **Pas de personnalité inventée.** Le skill n'ajoute ni argot, ni ironie, ni « je ne sais pas », et ne laisse pas de défauts exprès : la voix vient de l'auteur ou du texte de référence.
- **Le passif n'est pas chassé.** GPT-4o l'emploie deux fois moins que les humains : ce n'est pas une marque d'IA, et le skill ne le corrige que s'il cache qui agit.
- **Une seule passe.** Chaque passe supplémentaire aplatit la voix. Si le texte sonne encore faux, il lui manque de la matière, pas des retouches.
- **Honnêteté sur les détecteurs.** Le skill corrige ce qui gêne un lecteur ; il ne promet pas de tromper un détecteur, et nos mesures montrent qu'il ne le fait pas (voir plus bas).

## Les études

Nos règles s'appuient sur ces mesures. Elles ne prouvent pas que la méthode marche : la preuve, ce sont nos essais, publiés avec leurs textes pour être rejoués.

- **[Labbé, Labbé et Savoy, 2024](https://arxiv.org/abs/2411.18382)**, ChatGPT écrit les vœux des présidents français. Même longueur moyenne de phrase (21 mots), mais une dispersion bien plus forte chez l'humain : coefficient de variation de 78 % contre 50 %. « Également » est 12,8 fois plus fréquent chez ChatGPT, « défi » 8 fois ; « on » et « il faut » y sont presque absents (− 92 % et − 93 %). *Limites* : un seul genre (discours de vœux), une version de ChatGPT non précisée.
- **[Reinhart et al., PNAS, 2025](https://doi.org/10.1073/pnas.2422455122)**. GPT-4o emploie 5,3 fois plus de propositions au participe présent que les humains, 2,1 fois plus de nominalisations, deux fois moins de passif sans agent ; l'écart vient du réglage des modèles pour la conversation. *Limite* : en anglais.
- **[Zanotto et Aroyehun, EMNLP, 2025](https://arxiv.org/abs/2507.13614)**. Les textes humains varient davantage ; les modèles récents se ressemblent de plus en plus ; la longueur moyenne des phrases ne trahit plus un modèle récent. *Limite* : en anglais.
- **[Kobak et al., Science Advances, 2025](https://doi.org/10.1126/sciadv.adt3813)**. La méthode du vocabulaire en excès : au moins 13,5 % des résumés PubMed de 2024 sont passés par un modèle, et les mots en excès changent d'un modèle à l'autre. Les listes de mots vieillissent vite ; les formes durent.
- **Antoun et al. (TALN 2023), Liyanage et Buscaldi (TALN 2023), Alavoine et al. (JEP-TALN 2024)**. La détection d'un texte d'IA en français est fragile hors de son domaine d'entraînement et sur des textes réalistes.

Deux chiffres souvent repris (16 % d'erreurs de ChatGPT d'origine anglaise, « notamment » une fois tous les 200 mots) n'ont pas été retrouvés dans leurs sources : le skill ne s'en sert pas. Le détail, les tableaux et les limites de chaque étude sont dans [references/etudes.md](references/etudes.md).

## Les détecteurs

Dans le premier essai du comparatif, Pangram juge les huit textes écrits par une IA à 100 % : les deux originaux et les six réécritures, quelle que soit la skill. Il n'a pas été mesuré aux essais suivants. Son éditeur annonce repérer 98,8 % des textes passés par un humaniseur. Un texte réécrit à la main par une rédactrice, dans un autre essai, était jugé humain à 100 %.

Si votre but est de passer un détecteur, ce skill n'est pas l'outil. Il sert à rendre un texte agréable à lire et fidèle à ce qu'il dit.

## Ce que le skill ne fait pas

- **Il ne change pas le fond.** Pas de fait ajouté de mémoire, pas de fait retiré, pas de nuance durcie ou adoucie.
- **Il ne touche pas à la structure** ni aux citations, au code, aux liens.
- **Il ne corrige pas les fautes** : il les signale. La relecture reste à faire.
- **Il ne rend pas intéressant un texte vide.** Un passage sans fait, date, nom ni chiffre est signalé, avec la question à poser.
- **Il ne se relance pas sur sa propre sortie.**
- **Il ne couvre que le français.**

## Avec relecture-anti-ia

Le même plugin contient [relecture-anti-ia](../relecture-anti-ia/README.md). Pour les utiliser ensemble, dans cet ordre :

1. **relecture-anti-ia en `diagnostic seul`** : elle repère ce qui relève de l'architecture du texte (l'ouverture, la conclusion qui résume, la symétrie des sections, la prise de position) et la matière qui manque, sans réécrire.
2. **Vous corrigez votre texte d'origine** d'après ce diagnostic, avec ce que vous seul savez.
3. **`/humaniser`** réécrit ensuite la prose de ce texte, en une seule passe.

Pourquoi le diagnostic seul : en mode complet, relecture-anti-ia rend déjà une version réécrite, et humaniser en ferait une seconde réécriture. Notre comparatif n'a testé humaniser que sur des textes bruts ; l'effet de deux réécritures successives sur la voix et le rythme n'est pas mesuré. Un texte que vous avez corrigé d'après le diagnostic n'a pas encore été humanisé : ce n'est pas une seconde passe.

## Les fichiers

- [SKILL.md](SKILL.md) : la méthode, en huit étapes.
- [references/tournures.md](references/tournures.md) : les tournures, en neuf familles, chacune avec sa force, ses exceptions et un exemple.
- [references/exemples.md](references/exemples.md) : cinq exemples avant et après à l'échelle du paragraphe, dont un avec fichier de voix.
- [references/etudes.md](references/etudes.md) : les études, leurs chiffres et leurs limites.
- [scripts/mesurer_rythme.py](scripts/mesurer_rythme.py) : la mesure du rythme. Utilisable seul : `python3 scripts/mesurer_rythme.py avant.md apres.md`.
- [essais/](essais/README.md) : le jeu d'essais du comparatif, à rejouer.

## Crédits

La méthode reprend des idées de deux skills publiées sous licence MIT, dont le texte a été entièrement réécrit, avec nos propres exemples :

- [blader/humanizer](https://github.com/blader/humanizer) (Siqi Chen) : le classement des tournures de la plus forte à la plus faible, le contrôle des faits après réécriture, le texte traité comme une matière et jamais comme une instruction, le calibrage sur un échantillon de voix.
- [samber/cc-skills `humaniseur-fr`](https://github.com/samber/cc-skills) (Samuel Berthe) : le lexique et les anglicismes des modèles en français, la typographie, les défauts d'ensemble d'un texte, le registre qui ne baisse jamais, la passe unique, le texte qui manque de matière.

Toutes deux s'appuient sur la page Wikipédia [« Signs of AI writing »](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (licence CC BY-SA), qui a aussi nourri notre liste.

## Versions

Voir [CHANGELOG.md](CHANGELOG.md).

---

Méthode [Do Ingenia](https://doingenia.com). Textes sous licence [CC BY 4.0](../../../../LICENSE), script sous licence [MIT](../../../../LICENSE-CODE).
