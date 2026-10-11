---
name: empreinte-externe
description: Relève ce que le registre de l'État, Pappers, LinkedIn, Wikidata, Wikipedia et la fiche Google disent d'une entreprise française, le compare à son site et liste les écarts à corriger, du plus important au plus mineur. Montre d'où viennent les erreurs qu'une IA fait sur une entreprise (ancienne page LinkedIn, fiche oubliée, homonyme). À utiliser quand on demande d'« auditer mes fiches », de vérifier son « empreinte en ligne », de comprendre « pourquoi ChatGPT se trompe sur mon entreprise ». Option « réponses IA » pour rapprocher chaque erreur d'une IA de l'écart qui l'explique.
argument-hint: "[entreprise] [url du site] [siren : …] [réponses IA : …] [en fichier]"
---

# Empreinte externe

Quand une IA se trompe sur une entreprise, l'erreur vient souvent d'une fiche oubliée : une ancienne page LinkedIn, une fiche Pappers, un homonyme sur Wikidata. Ce skill relève ce que ces sources disent de l'entreprise, le compare à son site et liste les écarts à corriger, du plus important au plus mineur. L'utilisateur sait ainsi quelle fiche corriger, fermer ou revendiquer.

Le skill relève et propose. Il ne modifie rien lui-même.

## Périmètre

Version 1 : les entreprises françaises. L'ancre du relevé est le SIREN, lu dans le registre de l'État. Pour une entreprise immatriculée hors de France, le skill le dit dès le début et produit un relevé partiel, sans registre, signalé comme tel (voir l'étape 2).

## Entrée

- Le nom de l'entreprise et l'URL de son site. Les deux sont nécessaires.
- Facultatif : le SIREN. S'il est donné, il passe avant celui du site, mais le skill vérifie qu'il correspond bien à l'entreprise.
- Facultatif : « réponses IA », des textes que ChatGPT, Perplexity ou un autre assistant a donnés sur l'entreprise, collés par l'utilisateur. Voir l'étape 4.
- Facultatif : « en fichier » ou « en Markdown ». Voir la section « Où rendre la sortie ».

**Si rien n'est précisé**, ou si l'utilisateur ne donne que des options, ne jamais reprendre une entreprise vue plus tôt dans la conversation : afficher l'aide (section suivante) et demander le nom de l'entreprise et l'adresse de son site. **Si un seul des deux manque**, ne demander que celui-là, sans afficher l'aide. Reprendre une entreprise précédente seulement si l'utilisateur le demande explicitement.

## Aide

Si l'utilisateur écrit « aide », « options », ou lance le skill sans argument, ne rien relever et répondre uniquement par ce tableau, suivi de l'exemple, puis demander le nom de l'entreprise et l'adresse de son site :

| Ce que vous écrivez | Effet |
|---|---|
| `siren : 123 456 789` | Impose le SIREN au lieu de le lire dans les mentions légales. |
| `réponses IA : …` | Colle ce qu'une IA répond sur votre entreprise. Chaque erreur est rapprochée de l'écart qui l'explique. |
| `en fichier` ou `en Markdown` | Le relevé est écrit dans un fichier `.md`. |

Il faut au minimum le nom de l'entreprise et l'adresse de son site.

Exemple : `Relève l'empreinte externe de Maison Verdier Conseil, maisonverdier-exemple.fr, en fichier`

## Garde-fous (prioritaires sur toutes les étapes)

1. **Vérifier chaque mention avant de la retenir.** Une page qui remonte sur le nom de l'entreprise peut parler d'une autre. Contrôler au moins un élément qui relie la page à l'entreprise (SIREN, site, ville, dirigeant, activité) avant de la ranger dans le tableau.
2. **Trier le bruit.** LinkedIn et Wikidata remontent d'autres structures, parfois sans rapport (un jeu de société, un homonyme étranger). Ne garder que ce qui concerne l'entreprise ou un homonyme plausible.
3. **Données personnelles : empreinte professionnelle seulement.** Jamais de date de naissance ni d'adresse personnelle d'un dirigeant, même si une source l'affiche : ne pas la recopier, ne pas la citer. Dirigeant : nom et fonction seulement. Personne morale dirigeante : la nommer, ne pas deviner qui est derrière.
4. **Ne rien inventer.** Un fait introuvable s'écrit « non trouvé ». Une source qu'on n'a pas pu lire s'écrit « inaccessible » et figure dans les limites du relevé. Jamais de case remplie par déduction.
5. **Ne rien modifier soi-même.** Le skill propose, l'utilisateur agit. Aucune fiche n'est éditée, aucun formulaire envoyé, aucune page revendiquée.
6. **Ne jamais retenir un SIREN trouvé par une recherche sur le nom.** Une recherche par nom ne remonte que des homonymes. Le SIREN vient des mentions légales du site ou de l'utilisateur.
7. **Rester dans le relevé.** Chaque fait écrit vient d'une source lue pendant ce relevé et listée sous le tableau. Aucune référence, aucun client, aucun chiffre tiré de sa mémoire ou d'une page qui n'est pas dans les sources.
8. **Pas de conseil éditorial.** Le skill relève des désaccords entre sources. Il ne conseille ni style typographique, ni optimisation de fiche (horaires, photos, description), ni création de page Wikipedia.

## Étapes

### 1. Lire le site

Lire les mentions légales, la page À propos et la page contact. Pour les trouver, suivre les liens du menu et du pied de page de l'accueil, puis essayer les chemins usuels (`/mentions-legales/`, `/a-propos/`, `/contact/`). Une page introuvable est notée dans les limites. Pour les mentions légales, lire la page en entier : la forme juridique, le capital et le RCS arrivent parfois après une longue politique de confidentialité.

En tirer les faits d'identité tels que le site les annonce : nom de marque, raison sociale, forme juridique, date de création ou « depuis », dirigeants, activité, siège et zones d'intervention, appartenance à un groupe. Chercher aussi le SIREN, qui peut s'écrire :

- `SIREN 123 456 789` ;
- `SIRET` : les 9 premiers chiffres des 14 sont le SIREN ;
- `RCS <ville> 123 456 789` ou `RCS <ville> B 123 456 789`.

### 2. Ancrer sur le SIREN

- **Un SIREN trouvé, ou donné par l'utilisateur** : le retenir, puis le vérifier à l'étape 3 (le nom du registre doit correspondre à l'entreprise).
- **SIREN donné par l'utilisateur et différent de celui du site** : retenir celui de l'utilisateur et signaler la différence comme un écart (mentions légales à corriger), sauf si le registre montre que ce SIREN est celui d'une autre entreprise.
- **Plusieurs SIREN dans les pages du site** : si les mentions légales désignent clairement l'une des sociétés comme l'éditeur du site ou l'entité de la marque, la retenir. Les autres sont des sociétés du même groupe : les signaler en partie 3. Si rien ne permet de choisir, **s'arrêter** et demander laquelle est visée.
- **Aucun SIREN** : **s'arrêter**. Dire ce qui a été trouvé (ou pas) et demander le bon SIREN. Ne rien relever d'autre avant la réponse.
- **Entreprise manifestement immatriculée hors de France** (mentions légales qui citent un registre étranger, une adresse et une forme juridique étrangères, ou, à défaut de mentions lisibles, des sources tierces concordantes comme Wikidata ou un registre étranger) : ne pas demander de SIREN. Annoncer en première ligne que le relevé est partiel, sans registre français, puis relever le site, LinkedIn, Wikidata, Wikipedia et la fiche Google. La colonne Registre du tableau porte « hors périmètre (entreprise non immatriculée en France) ». Si le doute existe, demander si l'entreprise est immatriculée en France, et relever en partiel en attendant la réponse. Une entité française d'un groupe étranger peut exister : le dire dans les limites, sans la chercher par le nom.

### 3. Collecter

Utiliser la recherche web et la lecture de pages disponibles. Aucune clé d'API n'est nécessaire. Chercher le nom de marque, et la raison sociale quand elle diffère. Une source inaccessible est notée avec la raison, jamais tue.

**Registre de l'État** (API publique, gratuite)

- `https://recherche-entreprises.api.gouv.fr/search?q=<SIREN>` : garder le résultat dont le `siren` est exactement celui cherché. Lire `nom_complet`, `nom_raison_sociale`, `sigle`, le nom commercial et les enseignes du siège, `nature_juridique` (un code à traduire, par exemple 5710 pour une SAS), `activite_principale` (code NAF), `date_creation`, `etat_administratif`, `dirigeants` (nom, prénoms ou dénomination, qualité ; les commissaires aux comptes ne sont pas des dirigeants), `siege.adresse`, le nombre d'établissements.
- Si l'outil de lecture résume la réponse au lieu de la donner brute, demander les champs un par un et recopier la date de création et le code juridique tels quels : un résumé peut les déformer. En cas de doute entre deux lectures, relire.
- Le registre peut renvoyer des dates de naissance de dirigeants : les ignorer (garde-fou 3).
- Le nom du registre doit correspondre à l'entreprise du site. Sinon, le dire et demander confirmation du SIREN.
- Une seconde recherche, `?q=<nom>&per_page=10`, **uniquement pour repérer les homonymes** : écarter l'entreprise elle-même, noter les autres structures au même nom ou à un nom proche.

**Pappers**

- Page publique `https://www.pappers.fr/entreprise/<SIREN>` : dénomination, nom commercial, forme juridique, date de création, activité, siège, dirigeants. Pappers reprend le registre : un écart avec le registre est une erreur de lecture ou de mise à jour, pas une correction à faire chez Pappers.
- Si Pappers est inaccessible (par exemple une erreur 403), se rabattre sur la fiche societe.com de l'entreprise, trouvée par recherche web sur le **SIREN** (jamais sur le nom). Vérifier que la fiche porte bien ce SIREN. Dans la cellule du tableau, écrire « via societe.com : … » et le dire dans les limites. Si societe.com est aussi inaccessible, écrire « inaccessible ».

**LinkedIn** (lu sans compte, donc partiel)

- Recherche web de `"<nom>" LinkedIn entreprise` et `"<nom>" fondateur dirigeant LinkedIn`. Le lien LinkedIn affiché dans le pied de page du site est aussi une piste : vérifier qu'il mène à la bonne page. Garder les pages entreprise (`linkedin.com/company/…`). Chercher en particulier une **seconde page** pour la même entreprise : un doublon est une source classique de confusion.
- Relever pour chaque page : nom affiché, secteur, taille, siège ou localisation, année de création (« Founded »), site indiqué.

**Wikidata et Wikipedia**

- Wikidata : recherche d'entités au nom de la marque, en français et en anglais (`https://www.wikidata.org/w/api.php?action=wbsearchentities&search=<nom>&language=fr&format=json`), puis en plein texte sur la marque (`action=query&list=search&srsearch=<nom>`). L'entité qui porte le SIREN se cherche avec `srsearch=haswbstatement:P1616=<SIREN>` (P1616 est la propriété SIREN). Pas de recherche plein texte sur la raison sociale : elle ne remonte que du bruit.
- Wikipedia en français : recherche du nom entre guillemets, pour savoir si une page ou un article cite l'entreprise.
- Noter surtout les entités au même nom qui ne sont pas l'entreprise : si l'homonyme a une fiche et pas l'entreprise, c'est un risque de confusion.

**Fiche Google**

- Ce que la recherche web en montre (`<nom> <ville>`) : nom affiché, catégorie, adresse, site, éventuels doublons. Relevé partiel : on ne voit ni qui administre la fiche ni si elle est revendiquée. Une fiche que la recherche web ne montre pas peut exister : écrire « non visible par la recherche web », jamais « n'existe pas », et conseiller de la chercher directement dans Google Maps.

### 4. Option « réponses IA »

Si l'utilisateur a collé des réponses d'assistants, extraire chaque affirmation sur l'entreprise (nom, date, dirigeant, activité, lieu, groupe), puis la comparer au tableau.

- Écrire « correspond mot pour mot à » seulement si la source dit exactement la même chose et que c'est vérifiable dans le relevé.
- Sinon écrire « cohérent avec, non prouvé ».
- - Une affirmation fausse qu'aucun écart n'explique reste sans explication : la lister avec la mention « sans explication dans les sources relevées ». Ne pas en chercher une de force.
- Une affirmation correcte n'est pas listée.

### 5. Comparer et classer

Remplir le tableau des faits (section Sortie), puis relever les écarts.

**Un écart, c'est :**
- deux sources qui donnent des valeurs différentes pour le même fait ;
- une entité confondue avec l'entreprise (doublon, homonyme qui occupe la place) ;
- un lien manquant entre la marque, la raison sociale et le SIREN, quand la marque et la raison sociale diffèrent ;
- une fiche qui devrait exister et que les sources montrent absente (par exemple un site qui renvoie vers une page LinkedIn introuvable).

**Ce n'est pas un écart :** un fait absent d'une page où il n'a pas à figurer (la date de création n'est pas obligatoire dans les mentions légales), une différence de casse ou de ponctuation, un historique (ancien siège), une fiche qui n'existe pas faute de notoriété, un fait confirmé partout. Ne rien remplir pour atteindre un nombre.

Classer du plus structurant au plus mineur :

1. une entité confondue avec l'entreprise (doublon, homonyme qui occupe la place) ;
2. un lien manquant entre la marque, la raison sociale et le SIREN ;
3. un fait d'identité qui diverge (forme juridique, date de création, dirigeants, siège, activité) ;
4. une fiche attendue et introuvable, ou périmée ;
5. un détail de forme qui change le sens (une orthographe de nom différente, un libellé d'activité contradictoire).

## Le tableau des faits

Six colonnes, pas une de plus : Site, Registre, Pappers, LinkedIn, Wikidata/Wikipedia (une seule colonne pour les deux), Fiche Google. Les liens des sources sous le tableau. Règles de remplissage :

- **Fiche Google** : seulement ce que la fiche elle-même montre. Un annuaire ou une page tierce qui la recopie n'est pas la fiche : écrire « non visible par la recherche web ».
- **Pappers** : la date de création est celle de l'entreprise, pas celle d'un établissement ou d'un transfert de siège. Si elle n'est pas lisible, « non trouvé ». Un repli sur societe.com s'écrit « via societe.com : … » dans chaque cellule concernée.
- **Dirigeants** : nom d'usage et fonction (« Prénom Nom, président »). Pas les prénoms d'état civil complets. Les mêmes huit faits pour toutes les entreprises :

| Fait | À lire |
|---|---|
| Nom | marque, raison sociale, nom commercial et enseigne déclarés au registre |
| SIREN | mentions légales, registre, Wikidata |
| Forme juridique | mentions légales contre la nature juridique du registre |
| Création | date annoncée par le site contre registre, Pappers, LinkedIn (« Founded ») |
| Dirigeants | nom et fonction seulement ; personne morale : la nommer, ne pas deviner qui est derrière |
| Activité | code NAF, catégorie Google, secteur LinkedIn, contre le positionnement du site |
| Siège et zone | siège légal, adresses LinkedIn et Google, villes citées par le site |
| Groupe | appartenance annoncée par le site, visible ou non chez les tiers |

Une case vide s'écrit « non trouvé » ou « inaccessible », selon le cas.

## Sortie

Cinq parties, dans cet ordre.

### 1. Tableau des faits

Le tableau ci-dessus, avec les liens des sources dessous. Si le relevé est partiel (entreprise étrangère, source bloquée), une ligne le dit juste avant le tableau.

### 2. Écarts à corriger

Numérotés, du plus structurant au plus mineur. Pour chacun :

- **ce qui diffère**, et entre quelles sources ;
- **l'action** : corriger, fermer, revendiquer, déclarer ou créer. « Créer » ne concerne que ce qui est attendu et manquant (par exemple une page de mentions légales, un nom commercial non déclaré) ;
- **où la faire**. Repères : un nom commercial ou une forme juridique se déclarent au registre, par le guichet unique des formalités d'entreprises ; une fiche Google se revendique depuis le compte de gestion de la fiche ; un doublon de page LinkedIn se signale à LinkedIn par le formulaire d'aide, depuis la page à fermer ; une entité Wikidata ne se crée que si des sources indépendantes décrivent l'entreprise ; Pappers reprend le registre, donc se corrige à la source.

S'il n'y a aucun écart, le dire en une phrase plutôt que d'en chercher.

### 3. Homonymes

Seulement les structures qui portent **le même nom** que la marque ou la raison sociale (ou le même nom avec une forme juridique différente). Un nom proche, une partie du nom ou un homonyme étranger sans lien avec le secteur ou la zone n'est pas un homonyme : ne pas le lister. Pour chacun, dire pourquoi la confusion est plausible (même secteur, même zone, fiche plus visible que celle de l'entreprise). Ne pas attribuer de niveau de risque (« élevé », « faible ») sans élément qui l'étaye. Aucun homonyme exact : le dire en une phrase.

- Une société dont l'entreprise est dirigeante, ou qui la dirige, ou qui est citée par le site comme appartenant au même groupe, n'est pas un homonyme : c'est une société liée. La signaler comme une question à l'utilisateur (« cette société fait-elle partie de votre groupe ? »).
- Les entrepreneurs individuels homonymes sont comptés, pas nommés : leur nom est celui d'une personne. Sur un nom très courant, le registre renvoie des milliers de résultats : lire la première page, affiner par département ou activité si possible, et écrire « non comptés » plutôt qu'un zéro que rien ne prouve.

### 4. Erreurs des IA rapprochées

Seulement si l'option « réponses IA » est utilisée. Un tableau : l'affirmation de l'IA, le fait vérifié, l'écart qui l'explique, et l'une des trois mentions « correspond mot pour mot », « cohérent avec, non prouvé » ou « sans explication dans les sources relevées ».

### 5. Limites du relevé

Les sources inaccessibles, LinkedIn lu sans compte (donc partiel), la fiche Google vue par la recherche web (donc partielle), tout fait non vérifiable. Si l'outil de lecture ne renvoie qu'un résumé des pages et des réponses d'API, le dire : les valeurs sont celles du résumé. Une ligne par limite.

## Où rendre la sortie

- **Par défaut** : dans la conversation, les cinq parties l'une après l'autre.
- **Demande « en fichier » ou « en Markdown »** (si l'environnement permet d'écrire des fichiers) : écrire `<entreprise>.empreinte-externe.md` dans le dossier de travail, avec le nom de l'entreprise en minuscules et tirets. Si ce fichier existe déjà, ajouter la date : `<entreprise>.empreinte-externe-AAAA-MM-JJ.md`. Dans la conversation, donner seulement le chemin, les trois écarts les plus importants et les limites.
- **Si l'environnement ne permet pas d'écrire de fichier** : rendre le tout dans la conversation, dans un seul bloc de code ouvert par ```` ```markdown ````, prêt à être enregistré.

Le fichier commence par un en-tête :

```yaml
---
type: empreinte-externe
date: AAAA-MM-JJ
entreprise: "nom de marque"
siren: "123456789" ou "hors périmètre"
ecarts: 0
---
```

Puis les cinq parties, sous les titres `## 1. Tableau des faits`, `## 2. Écarts à corriger`, `## 3. Homonymes`, `## 4. Erreurs des IA rapprochées` (si utilisée) et `## 5. Limites du relevé`.

## Exemple court

Entreprise fictive : **Maison Verdier Conseil**, site `maisonverdier-exemple.fr`, SIREN fictif 123 456 789 (ni l'entreprise ni ce numéro n'existent).

**Extrait du tableau**

| Fait | Site | Registre | LinkedIn |
|---|---|---|---|
| Création | « depuis 2009 » | 14/03/2016 | Founded 2009 |
| Forme juridique | SARL | SAS | non trouvé |

**Écarts à corriger**

1. **Deux pages LinkedIn pour la même entreprise.** La page principale (Lyon, 12 salariés) et une page ancienne « Verdier Conseil » (Villeurbanne, 1 salarié, aucune activité). Action : fermer ou fusionner la page ancienne, depuis son formulaire d'aide.
2. **Date de création : 2009 sur le site et sur LinkedIn, 2016 au registre.** À vérifier avec le dirigeant : si 2009 est la date de début d'activité sous une autre forme, l'écrire sur le site (« activité depuis 2009, société créée en 2016 »). Action : corriger le site.
3. **Forme juridique : SARL sur le site, SAS au registre.** Action : corriger les mentions légales.

**Erreurs des IA rapprochées** (une IA annonçait « fondée en 2009 ») : cohérent avec l'écart 2, non prouvé : l'IA ne cite aucune source.

---

*Méthode Do Ingenia, adaptée pour fonctionner seule. Plus de détails : [doingenia.com/nos-outils/skills](https://doingenia.com/nos-outils/skills/). Licence CC BY 4.0.*
