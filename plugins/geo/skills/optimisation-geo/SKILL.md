---
name: optimisation-geo
description: Rend un article français (URL, fichier ou texte collé, publié ou brouillon) plus citable par les IA, pour le SEO et GEO et le référencement IA (AEO), en ajoutant seulement ce qui manque à sa forme, résumé en tête, tableau tiré de ses données, FAQ de questions réelles. Les ajouts sont surlignés, aucune phrase de l'auteur n'est réécrite, aucun fait n'est ajouté, et un script contrôle le résultat mot pour mot. Propose aussi un titre, des H2 en question et des sources à trouver, et signale passages vagues et dates dépassées. À utiliser quand on demande de « rendre un article citable », d'« optimiser un article pour le GEO » ou pour ChatGPT, d'« ajouter un résumé et une FAQ ».
argument-hint: "[url, @fichier ou texte] [questions : …] [intention : …] [diagnostic seul] [en fichier]"
---

# Optimisation GEO

Une IA reprend plus facilement un passage quand il se comprend seul et qu'il est facile à repérer : une réponse en tête, un tableau, une question suivie de sa réponse. Ce skill relève ce qui manque à la forme d'un article et l'ajoute, en surligné, à partir de ce que l'article dit déjà.

Il ne touche pas au texte de l'auteur et ne promet aucune citation. Il rend un article **citable**, pas cité : les facteurs qu'il suit sont des corrélations, et le skill le dit dans chaque diagnostic.

## Entrée

- L'article : une URL, un fichier ou un texte collé, déjà publié ou encore brouillon, en français.
- Facultatif : `questions : …`, des questions réelles (celles de vos clients, du support, de la Search Console).
- Facultatif : `intention : commerciale` ou `intention : informative`. Sinon, le skill la déduit et le dit.
- Facultatif : `diagnostic seul`. Le relevé, les propositions et les signalements, sans ajout.
- Facultatif : `en fichier`. Le diagnostic est aussi écrit dans un fichier. L'article avec ajouts l'est toujours.

**Si aucun article n'accompagne la demande**, ne jamais reprendre un texte vu plus tôt dans la conversation : afficher l'aide et demander l'article.

## Aide

Si l'utilisateur écrit « aide », « options », ou lance le skill sans article, ne rien traiter et répondre uniquement par ce tableau, suivi de l'exemple :

| Ce que vous écrivez | Effet |
|---|---|
| `questions : …` | Vos questions réelles pour la FAQ. Sinon, le skill les cherche sur le web. |
| `intention : commerciale` ou `informative` | Sert à juger si la page est ancienne. Sinon, elle est déduite. |
| `diagnostic seul` | Le relevé, les propositions et les signalements, sans ajout. |
| `en fichier` | Le diagnostic est aussi écrit dans un fichier `.md`. |

Exemple : `Optimise cet article pour le GEO : https://exemple.fr/blog/mon-article, intention : informative`

## Garde-fous (prioritaires sur toutes les étapes)

1. **Aucune réécriture.** Aucune phrase ni aucun titre de l'auteur n'est modifié, déplacé ou supprimé, même pour corriger une faute. Une faute se signale.
2. **Rien de nouveau sur le fond.** Aucun fait, chiffre, nom, exemple ou conseil qui ne soit déjà dans l'article. Ce qui manque au fond se signale, ne se comble pas.
3. **Rien n'est ajouté par principe.** Un élément n'est ajouté que s'il manque et si le contenu s'y prête. Sinon, le dire avec la raison. Un article déjà complet reçoit le verdict « rien à ajouter », et c'est une bonne réponse.
4. **Ajouts limités à 20 % des mots de l'article.** Ce plafond ne se négocie pas : ne jamais proposer de le dépasser. Sur un article court, il peut empêcher d'ajouter une FAQ : le dire, et donner les questions trouvées.
5. **Une question ne s'invente pas.** Toute question de FAQ vient de l'utilisateur ou d'une page trouvée pendant cette exécution, avec son lien.
6. **Jamais de promesse.** Écrire « citable », jamais « sera cité ». N'annoncer aucune hausse de citations ni de trafic.
7. **Aucun chiffre d'étude de mémoire.** Les seuls chiffres d'études autorisés sont ceux de [references/etudes.md](references/etudes.md), avec leur lien et leurs limites.
8. **Un brouillon reste privé.** Une recherche web porte sur le sujet, jamais sur des passages de l'article. Aucun article n'est envoyé à un service tiers.
9. **Un contrôle en échec ne se livre pas comme réussi.** Voir l'étape 7.

## Étapes

### 1. Obtenir l'article sans le reformuler

Le contrôle compare le résultat à cette copie : si elle est fausse, le contrôle ne vaut rien. Créer dans le dossier de travail `<nom>.original.md`, où `<nom>` vient du nom du fichier, de la fin de l'URL ou du titre, en minuscules et tirets. Les scripts sont dans le dossier `scripts/`, à côté de ce `SKILL.md`.

- **URL** : `python3 <dossier du skill>/scripts/lire_article.py "<url>" -o <nom>.original.md`. Le script donne aussi le titre de la page et ses dates, et liste les titres de la page qu'il n'a pas repris : ce sont en général des titres de menu ou d'articles similaires, mais si l'un appartient à l'article, le dire et demander le texte. Vérifier que le début et la fin correspondent bien à l'article, sans menu ni bloc d'articles similaires. Si ce n'est pas le cas, le dire et demander le texte. Ne pas retoucher le fichier à la main pour en retirer autre chose que ces restes de page, et le dire si on le fait.
- **Fichier** : le copier tel quel en `<nom>.original.md`. Le fichier de l'utilisateur n'est jamais modifié.
- **Texte collé** : l'écrire tel quel. S'il n'a aucun titre, ne pas en créer : le signaler.

**Si l'outil ne sait lire une page qu'à travers un résumé** (beaucoup d'outils de lecture web résument), ne pas s'en servir comme copie de référence : demander à l'utilisateur de coller l'article. Si le script renvoie le code 3 (site protégé, page chargée par JavaScript), faire de même.

Moins de 300 mots : s'arrêter et dire que le contenu est trop court pour être structuré. Article dans une autre langue que le français : s'arrêter et dire que le skill ne couvre que le français pour l'instant.

### 2. Relever la forme

`python3 <dossier du skill>/scripts/controle_ajouts.py --releve <nom>.original.md`

Le script donne les décomptes (mots, titres, tableaux, liens, années, débuts de section à relire). Lire ensuite l'article en entier et juger ce que le script ne peut pas voir :

| Élément | Question à trancher |
|---|---|
| Résumé en tête | Les 100 premiers mots donnent-ils déjà la réponse de l'article, même sans le mot « résumé » ? Si oui, il est présent. |
| Tableau | Y en a-t-il un avec une ligne d'en-tête ? Sinon, l'article contient-il des données comparables ? |
| FAQ | Y en a-t-il une, même sous un autre titre ou en gras ? Combien de questions ? |
| H2 en question | Combien ? |
| Titre | Est-il explicite ? Dépend-il d'une date ? |
| Sources | Les affirmations chiffrées ou réglementaires ont-elles un lien vers leur source ? |

### 3. Décider les ajouts

Pour chaque élément : ajouter ou non, avec la raison. Si « diagnostic seul » est demandé, ou si rien n'est à ajouter, ne créer aucun fichier d'article et passer à l'étape 8.

**Résumé.** Ajouter s'il n'y en a pas. Deux ou trois phrases qui donnent la réponse de l'article, prises dans ses propres termes, sur une seule ligne, juste sous le H1. Ne pas en ajouter si l'introduction donne déjà la réponse.

**Tableau.** Ajouter seulement si l'article contient des données comparables : chiffres, délais, critères, options comparées sur les mêmes attributs. Chaque cellule reprend ce que dit l'article. Ligne d'en-tête obligatoire. Un seul tableau, placé après le paragraphe qui porte les données, jamais à l'intérieur d'un paragraphe ou d'une liste. Une simple énumération ne fait pas un tableau. Sans données comparables : « pas de matière à tableau ».

**FAQ.** Ajouter seulement avec des questions réelles auxquelles l'article répond déjà :

1. Prendre les questions données par l'utilisateur.
2. Sinon, chercher avec la recherche web de l'outil, sur le sujet et une variante (`<sujet> questions fréquentes`, `<sujet> forum`). Une question compte si elle figure telle quelle sur une page trouvée : forum, questions associées affichées dans les résultats, FAQ d'un autre site, titre de page ou d'article formulé en question. Garder le lien et dire d'où elle vient. Ne pas la retoucher, sauf pour une faute ou une majuscule.
3. Si l'outil n'a pas de recherche web, ou si elle ne donne rien : pas de FAQ, et le dire. Ne jamais formuler soi-même une question « probable ».

Garder entre 3 et 6 questions. Moins de 3 : pas de FAQ, et donner dans le diagnostic les questions trouvées. La réponse (2 à 4 phrases) se tire du corps de l'article. Écarter une question déjà traitée par un H2, même formulée autrement (« Comment fonctionne un PBN ? » double le H2 « PBN : comment ça fonctionne ? »), ou en double avec une autre. Une question réelle à laquelle l'article ne répond pas est un manque de fond : la signaler, ne pas y répondre. Placer la FAQ à la fin de l'article, avant une éventuelle signature ou conclusion commerciale si elle se reconnaît clairement ; sinon tout à la fin.

**FAQ déjà présente.** Elle n'est ni réécrite ni réduite. Si elle compte moins de 6 questions, ajouter à sa suite les questions réelles manquantes, surlignées, jusqu'à 6. Si ses questions sont en gras plutôt qu'en titres, proposer de les passer en H3, sans l'appliquer. Une question douteuse (en double, sans réponse dans l'article) se signale.

**Plafond.** Si les ajouts dépassent 20 % des mots, retirer des questions de FAQ d'abord, le tableau ensuite, et le dire.

### 4. Écrire les ajouts

Copier `<nom>.original.md` en `<nom>.optimisation-geo.md`, puis **insérer les ajouts dans la copie avec un outil d'édition. Ne jamais retaper l'article** : c'est ainsi qu'un mot change sans qu'on le voie.

Chaque ajout est surligné `==…==` et occupe ses propres lignes, séparées du texte par une ligne vide :

```markdown
==**En bref** : [phrase 1]. [phrase 2]. [phrase 3].==
```

```markdown
| ==En-tête== | ==En-tête== |
|---|---|
| ==Valeur== | ==Valeur== |
```

```markdown
## ==Questions fréquentes==

### ==Question ?==

==Réponse.==
```

Jamais de surlignage au milieu d'une phrase d'origine. Les chiffres s'écrivent dans la forme de l'article (`1 200`, pas `mille deux cents`), sinon le contrôle les signale. Aucun tiret cadratin dans les ajouts, et le ton de l'article.

### 5. Préparer ce qui est proposé, sans l'appliquer

- **Titre** : une version en question si le titre n'en est pas une et si la question est naturelle. L'année seulement si le contenu dépend vraiment d'une date, et jamais une année que le contenu ne justifie pas. Sur une page en ligne, rappeler que changer un titre a un effet sur Google.
- **H2 en question** : une ou deux reformulations si aucun H2 n'est en question. Moins de 5 H2 : le signaler, sans découper l'article.
- **Sources à trouver** : les affirmations chiffrées ou réglementaires sans lien, citées telles quelles. Ne pas chercher soi-même une source pour les insérer : l'auteur vérifie.

### 6. Préparer les signalements, sans réécrire

Citer chaque passage tel quel, avec ce qui pose problème. Pas de reformulation proposée.

- **Passages vagues** : une affirmation sans nom propre ni chiffre qu'une IA ne pourrait pas reprendre utilement (« de nombreuses entreprises constatent de bons résultats »). Cinq au plus, les plus importants.
- **Sections qui ne se comprennent pas seules** : une section qui commence par « Il », « Cela », « Ce » ou un mot qui renvoie à la section précédente. Le relevé en donne une liste de départ : garder seulement les vrais cas. « Il existe trois formules » se comprend seul, « Il permet de gagner du temps » non.
- **Page ancienne selon l'intention** : déduire l'intention (commerciale : choisir, acheter, comparer ; informative : comprendre, apprendre), sauf si l'utilisateur l'a donnée. Repère de méthode, pas un seuil mesuré : à signaler au-delà de 12 mois sans mise à jour pour une page commerciale ou un sujet qui évolue vite ; une page informative sur un sujet stable peut vivre plus longtemps. Date inconnue ou brouillon : le dire. Ne jamais conseiller de changer la date sans changer le contenu.
- **Années dépassées** : une année passée présentée comme actuelle (« en 2023, le meilleur outil est… »), dans le titre ou le texte. Une étude datée citée comme telle n'est pas dépassée.
- **Fautes et incohérences** relevées au passage.

### 7. Contrôler

`python3 <dossier du skill>/scripts/controle_ajouts.py <nom>.original.md <nom>.optimisation-geo.md`

- **Code 0, réussi** : continuer. Lire les éventuels mots marqués « À VÉRIFIER » : un nom absent de l'article est à retirer de l'ajout.
- **Code 1, échec** : si le problème est dans vos ajouts ou votre copie, repartir de `<nom>.original.md`, refaire l'insertion, relancer. Deux essais au plus.
- **Toujours en échec, code 2, Python ou écriture de fichier indisponibles** : écrire en première ligne de la réponse « **Contrôle en échec : cet article n'est pas livré comme vérifié** » (ou « **Contrôle non effectué** »), avec la raison et la sortie du script. Ne pas écrire que l'article est intact.

Citer la ligne de résultat du script dans le diagnostic. Ne jamais déclarer un contrôle réussi sans avoir lu sa sortie.

### 8. Rendre le diagnostic

Dans la conversation, dans cet ordre :

1. **Verdict** : en une phrase, ce qui a été ajouté, ou « Rien à ajouter » si l'article a déjà sa structure. Puis le résultat du contrôle (si un article a été écrit).
2. **Relevé** : un tableau, une ligne par élément (résumé, tableau, FAQ, H2 en question, titre, sources) : présent ou non, et décision.
3. **Ajouts** : pour chacun, où et d'après quel passage de l'article. Pour la FAQ, chaque question avec sa source et son lien.
4. **Propositions, non appliquées** : titre, H2, sources à trouver.
5. **Signalements** : voir l'étape 6, et les questions réelles sans réponse dans l'article.
6. **Pourquoi ces éléments, et leurs limites** : deux ou trois lignes tirées de [references/etudes.md](references/etudes.md), seulement sur les éléments qui concernent cet article. Toujours inclure cette phrase : « Ce sont des corrélations, pas des causes : ces ajouts rendent l'article plus facile à citer, ils ne garantissent aucune citation. »
7. **Prochaine étape** : relire les surlignages, retirer les `==`, trancher les propositions. Si une FAQ est gardée, rappeler que l'étude mesure le balisage FAQPage, à poser à la publication.

## Où rendre la sortie

- **Article avec ajouts** : toujours `<nom>.optimisation-geo.md` dans le dossier de travail, à côté de `<nom>.original.md`. Ne jamais écraser un fichier existant : ajouter la date (`<nom>.optimisation-geo-AAAA-MM-JJ.md`). L'original de l'utilisateur et la page en ligne ne sont jamais modifiés.
- **Demande « en fichier »** : écrire aussi le diagnostic dans `<nom>.diagnostic-geo.md`, et ne donner dans la conversation que le verdict, le résultat du contrôle et les chemins.
- **Si l'environnement ne permet pas d'écrire de fichier ou de lancer Python** : le contrôle est impossible. Donner seulement les ajouts, chacun avec l'endroit où l'insérer, et écrire en première ligne « **Contrôle non effectué** ». Ne pas retaper l'article.

## Exemple court

Article fictif : « Comment choisir une chaudière à granulés », 900 mots, sans résumé, trois modèles comparés sur leur puissance et leur prix.

**Verdict** : résumé et tableau ajoutés, pas de FAQ (une seule question réelle trouvée). Contrôle : `RÉSULTAT : RÉUSSI`.

**Ajout, sous le H1**

```markdown
==**En bref** : Une chaudière à granulés se choisit d'abord sur sa puissance, puis sur son prix. Pour une maison de 120 m², l'article retient une puissance de 15 kW.==
```

**Proposition, non appliquée** : H2 « Le choix de la puissance » → « Quelle puissance choisir pour sa maison ? ».

**Signalement** : section « Entretien », première phrase : « Il reste simple. » ne se comprend pas sans la section précédente.

---

*Méthode Do Ingenia, adaptée pour fonctionner seule. Plus de détails : [doingenia.com/nos-outils/skills](https://doingenia.com/nos-outils/skills/). Textes sous licence CC BY 4.0, scripts sous licence MIT.*
