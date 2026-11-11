# Tournures d'un texte écrit par une IA

Liste lue par `/humaniser`. Chaque tournure porte sa force :

- **forte** : une seule occurrence justifie une correction ;
- **faible** : à corriger seulement si deux autres tournures se trouvent dans le même paragraphe.

Les mots à la mode changent avec chaque modèle ; les formes (opposition, chute, groupe de trois)
durent. Les familles A et B passent donc avant les listes de mots.

Aucune tournure ne se corrige dans une citation, un titre d'œuvre, un nom propre, ou un passage qui
parle de la tournure au lieu de l'employer.

Tous les exemples sont fictifs. Quand la version « après » porte un fait que la version « avant »
n'a pas, ce fait est supposé venir du fichier de voix ; sans source, on simplifie la phrase au lieu
de l'inventer (règle 2 de la skill). `references/exemples.md` montre le même geste à l'échelle du
paragraphe.

---

## A. Mettre en scène au lieu de dire

### A1. « Pas X, mais Y » (forte)

**Formes** : ce n'est pas X, c'est Y ; il ne s'agit pas de X mais de Y ; non seulement X, mais
aussi Y ; X plutôt que Y ; la même opposition étalée sur deux phrases (« Cela ne veut pas dire X.
Cela veut dire Y. ») ; la fin tronquée (« …, sans mauvaise surprise »).

**Pourquoi** : la première moitié nie une idée que personne n'a eue, pour grandir la seconde. On
garde l'opposition seulement si le lecteur croit vraiment X, ou si les deux moitiés apportent une
information.

> Avant : Un logiciel de paie n'est pas un simple outil, c'est un partenaire de votre croissance.
>
> Après : Le logiciel calcule les bulletins de 40 salariés en une heure, contre une journée à la
> main.

### A2. Phrase de chute (forte)

**Formes** : un paragraphe d'une phrase qui redit le précédent ; « C'est là toute la
différence. » ; « Tout est dit. » ; la même chute après chaque partie ; une phrase qui explique
l'exemple qu'on vient de lire (« Cet exemple montre bien l'importance de… ») ; une suite de
fragments (« Pas de délai. Pas de frais. Pas de stress. »).

**Pourquoi** : la phrase demande au lecteur de s'arrêter sans rien lui apporter. On la coupe ; on
la garde si elle ajoute un fait ou une conséquence. Les fragments se fondent en une phrase qui
affirme quelque chose de précis.

> Avant : Le devis arrive sous 48 heures. Pas d'attente. Pas de relance. Juste une réponse.
>
> Après : Le devis arrive sous 48 heures, sans qu'il faille relancer.

### A3. Fausse profondeur (forte)

**Formes** : au fond, la vraie question est, ce qui compte vraiment, en réalité, au cœur du
sujet, l'essentiel est ailleurs ; « X est le Y de Z » ; « X n'est pas un outil, c'est un miroir ».

**Pourquoi** : une idée ordinaire est habillée en vérité cachée. On dit l'idée.

> Avant : Au fond, la vraie question est celle de la confiance. La transparence est la monnaie
> de la relation client.
>
> Après : Le client signe quand il comprend ce qu'il paie : le devis détaille chaque poste.

### A4. Annonce avant le propos (forte)

**Formes** : plongeons dans, découvrons ensemble, voici ce qu'il faut savoir, dans cet article
nous allons, faisons le point, avant tout, soyons honnêtes, la vérité ?, disons-le franchement.

**Pourquoi** : le texte annonce ce qu'il va dire au lieu de le dire. On supprime l'annonce et on
commence par le contenu.

> Avant : Vous vous demandez combien coûte une isolation ? Faisons le point ensemble.
>
> Après : Une isolation des combles perdus coûte de 20 à 40 € le mètre carré, pose comprise.

### A5. Réponse à une objection absente (forte)

**Formes** : entendons-nous bien, il ne s'agit pas de dire que, loin de nous l'idée de, on
pourrait être tenté de, une approche tentante serait, certains diront que… mais.

**Pourquoi** : le texte répond à une critique que personne n'a faite, souvent un reste de
brouillon. On garde l'objection que le texte attribue à quelqu'un ou à laquelle il répond vraiment.

---

## B. Rythme mécanique

### B1. Groupes de trois (forte si répété, faible seul)

**Formes** : trois adjectifs, trois noms, trois exemples parallèles, trois faits suivis d'une
leçon. Les listes de 3, 5 ou 7 éléments par réflexe.

**Pourquoi** : les idées arrivent par trois pour sonner complet, que le sens en ait trois ou non.
On garde trois éléments quand il y en a trois ; sinon on fusionne ou on développe le plus fort.

> Avant : Un accompagnement simple, rapide et efficace.
>
> Après : Un seul interlocuteur, du devis à la mise en service.

### B2. Tirets cadratins partout (faible seul, forte en série)

Remplacer le tiret (— ou –, et ` -- `) par une virgule, deux-points, parenthèses ou un point, sauf
si l'échantillon de voix en use. Les tirets du code, des chemins et des liens restent.

### B3. Phrases toutes de même longueur (forte sur un texte entier)

Un modèle concentre ses phrases entre 15 et 39 mots ; le texte humain a des extrêmes, des phrases
très courtes et quelques longues. La moyenne est la même (21 mots chez les présidents comme chez
ChatGPT), l'écart non : coefficient de variation de 78 % contre 50 % (Labbé et al., 2024,
`etudes.md` § 1). Se mesure avec `mesurer_rythme.py` (étape 3bis de la skill).

### B4. Même attaque de phrase (faible)

Plusieurs phrases de suite qui commencent pareil (« Cette solution… Cette approche… Ce
dispositif… »). Varier le sujet ou commencer par l'action. Une répétition voulue pour le rythme
reste.

### B5. Précautions empilées (faible)

**Formes** : pourrait potentiellement, il semblerait que cela puisse, dans certains cas il est
possible que.

On garde une précaution quand la source la justifie, et toujours quand le secteur ou le fichier
de voix l'imposent (règle 4 de la skill). On retire seulement l'empilement.

> Avant : Cette aide pourrait potentiellement, dans certains cas, permettre de réduire la facture.
>
> Après : Cette aide peut réduire la facture, sous condition de revenus.

---

## C. Gonfler l'importance

### C1. Portée historique (forte)

**Formes** : marque un tournant, témoigne de, joue un rôle clé, s'inscrit dans une dynamique plus
large, ouvre la voie à, une étape décisive, un héritage durable ; les parties « Défis et
perspectives » ; « Malgré ces défis, … continue de prospérer » ; « L'avenir s'annonce
prometteur ».

**Pourquoi** : un fait ordinaire est relié à une grande tendance que personne n'a demandée. On
garde le fait, on retire la portée. On finit sur le dernier fait concret.

### C2. Langage de brochure (forte)

**Formes** : niché, au cœur de, incontournable, à couper le souffle, d'exception, un savoir-faire
unique, riche (au figuré), un véritable joyau, une expérience inoubliable.

**Pourquoi** : le texte vend au lieu de décrire. On dit ce qu'est la chose.

### C3. Autorité anonyme (forte)

**Formes** : les experts s'accordent, selon de nombreuses études, il est largement admis que, les
spécialistes recommandent ; la liste de médias où quelqu'un a été cité.

**Pourquoi** : une autorité sans nom tient lieu de preuve. On nomme la source si on la connaît
(dans le texte ou le fichier de voix), sinon on retire l'affirmation ou on la présente comme une
expérience de l'auteur.

### C4. Participe présent qui fait l'analyse (forte)

**Formes** : soulignant, reflétant, illustrant, contribuant à, garantissant, favorisant, mettant
en lumière, accolés à un fait simple.

**Pourquoi** : le participe ajoute une profondeur que le fait ne porte pas. C'est l'une des marques
les mieux mesurées : GPT-4o emploie 5,3 fois plus de propositions au participe présent que les
humains (Reinhart et al., 2025, `etudes.md` § 2). On garde le fait ; le lien de cause seulement si
une source le dit.

> Avant : Le chantier a duré deux jours, illustrant notre réactivité et garantissant un confort
> optimal.
>
> Après : Le chantier a duré deux jours ; la famille n'a pas eu à quitter la maison.

### C5. Fuir « être » et « avoir » (faible)

**Formes** : constitue, représente, fait office de, se positionne comme, dispose de, bénéficie de,
offre.

> Avant : L'entreprise dispose d'une équipe de six techniciens et se positionne comme un acteur
> de référence.
>
> Après : L'entreprise a six techniciens.

### C6. Nominalisations (forte en série)

**Formes** : la mise en place de, la réalisation de, la prise en compte de, l'optimisation de, la
mise en œuvre de, la gestion de ; un nom d'action là où un verbe suffit.

**Pourquoi** : GPT-4o emploie 2,1 fois plus de nominalisations que les humains (Reinhart et al.,
2025), et ChatGPT écrit en français 7 % de noms en plus que les présidents (Labbé et al., 2024 ;
`etudes.md` § 1 et 2). Le nom fige l'action et efface celui qui agit. On rend le verbe et son sujet.

> Avant : La mise en place de la solution permet une réduction des délais de traitement.
>
> Après : Depuis que nous l'utilisons, un dossier se traite en deux jours au lieu de cinq.

### C7. Lien flou (faible)

**Formes** : lié à, associé à, en lien avec, en relation avec, quand le texte pourrait dire
quelle est la relation. Si on ne la connaît pas, on garde le mot flou.

---

## D. Lexique français des modèles

### D1. Mots surreprésentés (faible un par un, forte en grappe)

**Mesurés en français** (Labbé et al., 2024, `etudes.md` § 1, fréquence chez ChatGPT face aux
présidents) : **également** (12,8 fois plus fréquent : + 1 178 %), **défi** (8 fois : + 696 %,
surtout dans « relever les défis », « face aux défis »).

**Relevés par l'usage, non mesurés en français** : crucial, essentiel, primordial, notamment, par
ailleurs, en outre, de plus, véritable, optimal, optimiser, permettre de, favoriser, garantir,
assurer, accompagner (au sens vague), levier, enjeu, dispositif, acteur, écosystème, dynamique,
solution (pour tout), sur-mesure, clé en main, serein, en toute sérénité, robuste, holistique.

Remplacer par le mot précis, un chiffre, ou rien. « Également » : un par texte court, un par
paragraphe au plus dans un texte long.

Ces listes vieillissent vite : les mots en excès changent avec les modèles (Kobak et al., 2025,
`etudes.md` § 4). Les formes (familles A, B, I) durent plus longtemps.

Attention : un mot de cette liste peut être un mot de l'auteur. S'il figure dans le fichier de
voix, il reste.

### D1bis. La grappe « devoir, continuer, tenir, nous » (forte en grappe)

ChatGPT emploie en français deux fois plus « devoir » (+ 101 %), bien plus « continuer » (+ 145 %)
et « tenir » (+ 158 %), et moitié plus « nous » (+ 51 %) que les présidents (Labbé et al., 2024).
Réunis (« nous devons continuer à tenir nos engagements »), ils donnent une phrase moyenne sans
action. On la réécrit autour d'un geste concret : qui fait quoi, quand.

### D1ter. Les pronoms et verbes qui manquent (faible un par un, forte sur un texte entier)

Le même corpus montre ce que ChatGPT n'écrit presque plus : « on » (− 92 %), « il faut »
(− 93 %), « dire » (− 78 %), et 22 % de pronoms en moins, au profit des noms et des adjectifs.

- Quand le registre le permet (article de conseil, texte courant), rendre « on » et « il faut » :
  « Il faut compter une demi-journée » plutôt que « La durée d'intervention est d'une
  demi-journée ».
- Remplacer un nom répété par un pronom quand le sens reste clair.
- Ne jamais forcer « on » ni « il faut » dans un texte soutenu, institutionnel, juridique ou de
  santé : « il convient de » peut devenir « mieux vaut », et une forme impersonnelle (« est
  proposé ») reste impersonnelle.

### D2. Formules d'ouverture et de clôture (forte)

À l'ère de, dans un monde où, dans un contexte de, dans le paysage actuel, aujourd'hui plus que
jamais, il est essentiel de noter que, il convient de souligner que ; en conclusion, en résumé, en
somme, en définitive, au final, en fin de compte, en tête du dernier paragraphe.

### D3. Remplissage (faible)

| Remplissage | Plus simple |
|---|---|
| afin de parvenir à | pour |
| en raison du fait que | parce que |
| à l'heure actuelle | aujourd'hui |
| dans l'éventualité où | si |
| être en mesure de | pouvoir |
| en ce qui concerne | pour, sur |
| procéder à l'installation | installer |

### D4. Synonymes en cascade (faible)

Le même objet nommé trois façons de suite (« le logiciel… l'outil… la solution… »). Un humain
répète le mot juste.

### D5. Doublets (faible)

simple et rapide, fiable et durable, clair et transparent, riche et varié : un seul mot, ou un fait.

---

## E. Anglicismes de modèle (forte)

| Anglicisme | Français |
|---|---|
| faire du sens | avoir du sens |
| adresser un problème | traiter un problème |
| impacter | toucher, affecter |
| supporter (= soutenir) | soutenir, prendre en charge |
| définitivement (= certainement) | sans aucun doute |
| délivrer (un service) | fournir, assurer |
| opportunité (= occasion) | occasion |
| initier (= lancer) | lancer, commencer |
| digital (hors usage installé de l'auteur) | numérique |
| virgule avant « et » dans une énumération | pas de virgule |

---

## F. Mise en forme par réflexe

### F1. Gras décoratif (forte en série)

Des mots en gras sans raison, des listes où chaque élément commence par un intitulé en gras suivi
de deux-points. On retire le gras ; une liste à intitulés devient une phrase quand les intitulés
n'apportent rien. **Exception** : une liste que le fichier de voix demande garde sa
forme ; on n'en réécrit que la prose.

### F2. Titres à l'anglaise et décorés (forte)

Majuscule à chaque mot (« Nos Solutions Pour Votre Maison »), émojis ou flèches en tête de titre
ou d'élément, filet entre chaque partie. En français, seule la première lettre et les noms propres
prennent la majuscule. Un intertitre en question reste une question (règle 3 de la skill).

### F3. Typographie incohérente (faible)

Guillemets droits, courbes et chevrons mêlés ; apostrophes droites et courbes mêlées ; espace
manquante avant « : ; ! ? » ; nombres à l'anglaise (1,500.50). On suit la convention déjà
majoritaire dans le texte, et on la tient partout. Ne jamais retirer une espace insécable.

### F4. Restes techniques (forte)

`**mot**` ou `##` non rendus, marques de citation de chat (`:contentReference[…]`), caractères
invisibles (U+200B, U+200C, U+200D, U+FEFF). Ne pas toucher aux espaces insécables (U+00A0, U+202F).

---

## G. Restes de conversation (forte)

### G1. Formules de chat

J'espère que cela vous aide, n'hésitez pas à, bien sûr !, excellente question, vous avez tout à
fait raison, voici un…, souhaitez-vous que je… On retire l'emballage, on garde le contenu.

### G2. Limites de connaissance

Selon les informations disponibles, à ma connaissance, bien que les détails soient limités, il
semblerait que… suivis d'une supposition. On dit ce que la source ne donne pas, ou on coupe.

### G3. Le texte qui parle de lui-même

« Le tableau ci-dessous compare… », « cette partie est organisée par… », « ce guide a été conçu
pour… ». On garde une indication seulement si le lecteur ne peut pas la deviner.

### G4. L'intertitre redit

Un intertitre suivi d'une phrase qui le répète avant le vrai contenu : on coupe la phrase.

---

## H. Construction d'ensemble

Ces défauts se voient à l'échelle du texte, même sans aucun mot signalé.

### H1. Annonce, résumé et écho (forte)

Une introduction qui annonce le plan, une conclusion qui le redit, une première phrase qui
reformule la question du titre. L'information est servie trois fois. On commence par du contenu ;
on finit sur une conséquence ou un fait que l'introduction ne laissait pas prévoir.

### H2. Catalogue sans angle (forte)

Des parties qu'on pourrait permuter sans rien casser : définition, avantages, inconvénients,
conseils, conclusion, toutes de même profondeur. On ne change pas l'ordre des intertitres ;
on donne à chaque partie une phrase de liaison qui s'appuie sur la précédente, et on le signale si
le texte n'a pas d'angle.

### H3. Moule de paragraphe (faible)

Chaque paragraphe : idée, deux arguments, mini-conclusion, ouvert par « Tout d'abord », « Ensuite »,
« De plus », « Enfin ». On retire les connecteurs d'échafaudage ; la juxtaposition suffit.

### H4. Faux équilibre (faible)

Chaque affirmation aussitôt nuancée (« Cependant, il convient de nuancer… »), « d'une part,
d'autre part », conclusion « tout dépend de votre situation ». On prend la position de l'auteur ; on
nuance une fois, là où ça compte, et on dit de quoi ça dépend.

### H5. Altitude constante (forte : manque de matière)

Tout le texte reste à mi-hauteur : aucune date, aucun nom, aucun prix, aucun cas. Ce n'est pas un
défaut de style : on remplit avec un fait du fichier de voix s'il existe, sinon on signale le passage
et la question à poser à l'auteur.

### H6. Aucune raison d'écrire (faible)

Rien ne dit pourquoi ce texte existe, pour qui, à quelle occasion. Si le fichier de voix en donne une (une
question fréquente des clients, un changement de règle, un cas vécu), l'ancrer dans les premiers
paragraphes.

---

## I. Marques des modèles récents

Les modèles bien guidés évitent les familles A à G. Il leur reste ces habitudes, plus discrètes,
relevées dans nos essais sur des textes entièrement écrits par une IA qui ne portaient presque
aucune tournure classique.

### I1. Deux-points en cascade (forte en série)

**Formes** : « Reste le délai : … » ; « Le cas simple : … Le cas complexe : … » ;
« X est clair : … » ; un intitulé, deux-points, puis la phrase, paragraphe après paragraphe.

**Pourquoi** : le deux-points évite de choisir le lien entre deux idées, comme le tiret en anglais.
Une ou deux fois, c'est de la ponctuation ; à chaque paragraphe, c'est un tic. On écrit le lien
(parce que, donc, alors) ou on fait deux phrases.

> Avant : Reste le délai : la mairie répond en deux mois.
>
> Après : La mairie répond en deux mois.

### I2. Formules de cadrage (forte)

**Formes** : tout se joue sur, méritent d'être vérifiés, c'est typiquement le cas, reste à, donne
un aperçu concret, est clair, ne change rien en revanche, au-delà de ces lignes.

**Pourquoi** : la formule annonce l'importance ou la clarté au lieu de la laisser au fait. On garde
le fait.

> Avant : Tout se joue sur l'isolation des murs.
>
> Après : L'isolation des murs pèse le plus sur la facture.

### I3. Paires symétriques (forte)

**Formes** : deux paragraphes bâtis sur le même moule (« Le cas simple : … Le cas complexe : … »,
même longueur, même ordre d'arguments) ; une liste de deux à puces suivie d'une liste de trois.

**Pourquoi** : la symétrie vient du modèle, pas du sujet : les deux cas n'ont presque jamais autant
à dire. On développe celui qui compte pour le lecteur et on raccourcit l'autre.

### I4. L'écho de la question (forte)

**Formes** : une première phrase qui redit le titre ou l'intertitre au lecteur (« Si vous
envisagez de…, vous vous êtes posé la question de… »).

**Pourquoi** : le lecteur vient de lire la question. On commence par la réponse ou par une scène
concrète.

### I5. Phrase-renvoi sans fait (faible)

**Formes** : une dernière phrase qui renvoie à d'autres exemples sans en donner un (« Les chantiers
menés à Lyon et à Nantes donnent un aperçu concret »).

**Pourquoi** : elle promet un fait et n'en donne pas. On donne le fait s'il est dans le texte ou
le fichier de voix, sinon on signale le manque.

### I6. Altitude et rythme constants (forte sur un texte entier)

Toutes les phrases entre 15 et 25 mots, tous les paragraphes de trois ou quatre phrases, aucune
phrase de moins de dix mots, aucune digression. Voir l'étape 3bis de la skill.

---

## Ce qu'on ne touche pas

- Une citation, un verbatim d'interview, un nom de produit ou de marque.
- Une précaution que le secteur ou le fichier de voix imposent.
- La structure : titre, intertitres, tableaux, FAQ, résumé, listes.
- Les détails qui portent la voix : un fait rare, une parenthèse sincère, une opinion de l'auteur,
  une hésitation qu'il assume.
- Le passif. Ce n'est pas une marque d'IA : GPT-4o emploie deux fois moins le passif sans agent que
  les humains (Reinhart et al., 2025). On ne le remplace que s'il cache qui agit alors que le
  lecteur a besoin de le savoir.
