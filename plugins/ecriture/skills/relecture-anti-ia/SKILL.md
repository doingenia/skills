---
name: relecture-anti-ia
description: Relit un texte en français (article, page de site, newsletter, post) pour retirer les tics d'écriture qui trahissent une rédaction par IA, sans inventer de faits et sans perdre le mot-clé visé. Produit un diagnostic règle par règle, une version corrigée et la liste des endroits où il manque de la matière terrain, dans la conversation ou dans un fichier Markdown. À utiliser quand on demande de « relire », « humaniser », « rendre moins IA », « retirer les marqueurs IA » ou de vérifier qu'un texte ne sonne pas généré. Mode « diagnostic seul » sur demande.
---

# Relecture anti-IA

Un texte généré par IA se reconnaît moins à ses mots qu'à ses réflexes : une ouverture qui pose le décor, des transitions trop lisses, des listes parfaitement équilibrées, une punchline à chaque fin de section, une conclusion qui résume ce qu'on vient de lire. Ce skill repère ces réflexes et les corrige.

Il ne rend pas un texte « humain » en lui ajoutant de faux souvenirs. Ce qui rend un texte impossible à confondre avec une production d'IA, c'est la matière que seul l'auteur possède : un cas vécu, un chiffre interne, une position qu'il assume. Quand cette matière manque, le skill le dit et laisse l'auteur la fournir.

## Entrée

- Le texte à relire, collé dans la conversation ou fourni sous forme de fichier (chemin ou pièce jointe).
- Facultatif : le type de texte (article, page de service, post, newsletter) et le public visé. S'ils ne sont pas donnés, les déduire du texte sans poser de question.
- Facultatif : le mot-clé principal visé. S'il n'est pas donné, le déduire du titre (ou du champ de mot-clé si le fichier en a un) et l'indiquer en tête du diagnostic.
- Facultatif : « diagnostic seul ». Dans ce cas, produire uniquement la partie 1 de la sortie et ne pas réécrire.
- Facultatif : « en fichier » ou « en Markdown ». Voir la section « Où rendre la sortie ».

## Garde-fous (prioritaires sur toutes les règles)

1. **Ne jamais inventer.** Aucun cas client, chiffre, date, nom, citation, anecdote ou expérience personnelle ne doit apparaître s'il n'est pas déjà dans le texte. Quand une règle demande de la matière que le texte ne contient pas (un récit, une nuance tirée du terrain, une prise de position), insérer un marqueur `[À COMPLÉTER : ce qu'il faudrait ici]` et l'ajouter à la partie 3 de la sortie.
2. **Ne pas changer le sens.** Les faits, chiffres, noms propres, termes techniques et engagements restent identiques. En cas de doute sur une reformulation, garder l'original.
3. **Ne pas toucher aux citations.** Un texte entre guillemets attribué à quelqu'un reste mot pour mot, même s'il enfreint une règle.
4. **Garder la voix de l'auteur.** Conserver son vocabulaire, son registre (tutoiement ou vouvoiement, niveau de langue) et ses expressions propres. Corriger les réflexes, pas la personnalité.
5. **Ne pas surcorriger.** Une rupture de rythme forcée se voit autant qu'un texte trop lisse. Si un passage fonctionne, le laisser.
6. **Garder le mot-clé principal.** Le mot-clé visé reste dans le titre et apparaît dans l'ouverture (les 100 premiers mots). Si une phrase supprimée ou réécrite le portait, le réintégrer naturellement dans la nouvelle ouverture. Ne jamais l'ajouter là où il n'était pas : on préserve le référencement, on ne le refait pas.

## Les 18 règles

Pour chaque règle : ce qu'on cherche, puis comment corriger.

### Ouverture

**1. Pas d'ouverture contextuelle.** Chercher une première phrase qui pose un décor général (« À l'heure où… », « Dans un monde de plus en plus… », « X est devenu un enjeu majeur »). Test : si on supprime la première phrase et que le texte ne perd rien, elle ne mérite pas d'exister. Corriger en ouvrant sur une tension : un cas concret, un chiffre qui surprend, une idée reçue que le texte va contredire. Si le texte n'en contient aucun, utiliser le marqueur `[À COMPLÉTER]`. Penser au garde-fou 6.

### Typographie

**2. Pas de tiret cadratin (—) ni de demi-cadratin (–) en incise.** En français courant, ce tiret est rare ; dans un texte généré, il est partout. Remplacer selon le cas : virgule pour une incise, deux-points pour une explication ou un titre avec sous-titre, parenthèses pour une précision, point pour couper en deux phrases. Les tirets de liste en début de ligne ne sont pas concernés.

### Rythme et structure

**3. Casser la symétrie.** Chercher des sections de longueur presque identique, des listes qui tombent sur un nombre rond (3, 5, 10), des éléments de liste tous traités au même niveau de détail. Corriger en variant la longueur des sections (en fusionner, en raccourcir une franchement), en développant davantage l'élément le plus important d'une liste. Ne pas ajouter d'éléments inventés pour casser un nombre rond : on peut en fusionner deux, ou en retirer un faible.

**4. Alterner les longueurs de phrases.** Chercher des paragraphes où toutes les phrases font à peu près la même longueur. Corriger en coupant une phrase longue, ou en isolant une affirmation courte après une explication.

**5. Une seule formule ternaire par texte.** Une formule ternaire, c'est un groupe de trois éléments rythmés pour faire effet : trois phrases courtes en cascade (« Plus simple. Plus rapide. Plus sûr. »), ou trois groupes parallèles (« pour comprendre, pour décider, pour agir »). En garder une, la meilleure. Reformuler les autres en phrases normales, ou en ramenant à deux ou quatre éléments si le contenu s'y prête.

**6. Pas de triptyque décoratif.** Chercher les énumérations dont les éléments disent presque la même chose (« clair, simple et accessible »). Ne garder que les éléments qui apportent chacun une information distincte.

### Transitions

**7. Supprimer les transitions passe-partout.** Chercher les phrases de liaison qui pourraient servir dans n'importe quel texte sur n'importe quel sujet : « Mais ce n'est pas tout. », « C'est là que tout se joue. », « Et c'est précisément là que… », « Cette différence a une conséquence directe : », ou une question de liaison qui reprend le titre. Corriger en supprimant la transition (on passe directement à l'idée suivante), en la remplaçant par une phrase ancrée dans le sujet, ou en enchaînant sur un exemple.

**8. Test de la fluidité suspecte.** Relire le texte d'une traite. Si rien n'accroche, si chaque paragraphe s'emboîte parfaitement dans le suivant, le texte est trop lisse. Introduire au moins deux ruptures : un saut direct d'une idée à l'autre, une phrase très courte, une question que le lecteur se pose.

### Répétitions et tournures

**9. La formulation clé n'apparaît qu'une fois.** Chercher l'argument martelé avec les mêmes mots à plusieurs endroits (hors citations). Garder la formulation exacte à l'endroit où elle porte le plus, varier ailleurs : autre angle, reformulation, intégration dans une phrase plus large.

**10. Pas de fausse opposition.** Chercher les tournures qui corrigent une idée que personne n'a avancée : « ce n'est pas X, c'est Y », « ce n'est pas simplement X : c'est avant tout Y », « X n'est pas qu'un Y », « il ne s'agit pas de X mais de Y », « plus qu'un X, un Y ». C'est l'un des tics les plus reconnaissables. Corriger en affirmant Y directement. Une seule peut rester si l'idée contredite est réellement répandue chez le lecteur et que le texte la nomme. Ne jamais en créer en réécrivant.

### Clôtures

**11. Pas de punchline à chaque fin de section.** Chercher les sections qui se terminent toutes par une formule frappante qui résume la morale du passage, ou par deux chutes de suite. Une ou deux peuvent rester. Les autres s'arrêtent simplement sur un fait, un exemple, ou enchaînent vers la suite.

**12. Pas de conclusion récapitulative.** Chercher un dernier paragraphe ou une dernière section qui redit ce qui a été démontré, un encadré « Ce qu'il faut retenir », ou un bloc de précautions regroupées en fin de texte. Test : relire les trois derniers paragraphes ; s'ils reformulent ce qui précède, couper. Les précautions et limites se replacent dans le corps du texte, à côté de l'affirmation qu'elles tempèrent. La fin peut revenir à l'angle de l'ouverture, poser une question qui reste en tête, ou s'arrêter quand l'argument est posé.

### Incarnation et position

**13. Au moins une prise de position assumée.** Chercher si le texte prend un risque : dire ce qu'on ne fait pas, contredire une pratique courante, assumer un choix. S'il reste neutre de bout en bout, repérer dans le texte une position implicite et la rendre explicite. S'il n'y en a aucune, utiliser le marqueur `[À COMPLÉTER : position à assumer sur …]`.

**14. Au moins un moment de nuance dans le corps du texte.** Un texte où tout s'emboîte parfaitement sonne faux. Chercher une limite, un cas où la solution ne suffit pas, une incertitude. Si le texte en contient une reléguée en fin de texte, la remonter à côté de l'affirmation concernée. S'il n'en contient aucune, utiliser le marqueur `[À COMPLÉTER : limite ou cas où ça ne marche pas]`.

**15. Raconter les cas, ne pas les lister.** Chercher les exemples alignés comme des preuves (« Nos clients : A, B et C ») ou les profils abstraits (« Les entreprises en croissance »). Si le texte contient les éléments d'un récit, les réorganiser en micro-récit de deux ou trois phrases : la situation, ce qui a été fait, le résultat. Si le récit manque, utiliser le marqueur.

**16. Intégrer la légitimité dans l'argument.** Chercher un encart isolé sur l'auteur ou l'entreprise (« Fondée en…, notre équipe de… »), surtout en ouverture ou en fin de texte. Déplacer ces éléments là où ils servent de preuve à une affirmation. Exception : quand le sujet même du texte est « qui vous accompagne », le parcours de l'auteur répond à la question et peut ouvrir le texte. En fin de texte, un appel à l'action se limite à une ligne.

**17. Pas d'affirmation orpheline.** Chercher les phrases isolées qui affirment un bénéfice sans rien pour l'étayer (« Le tri valorise aussi votre image. »), souvent restées après la suppression d'une formule ternaire. Les rattacher à un élément du texte qui les prouve, les supprimer si elles n'apportent rien, ou poser un marqueur `[À COMPLÉTER : preuve de …]` si l'idée mérite d'être gardée.

### Test final

**18. Le test ChatGPT.** Se poser la question : un lecteur qui aurait accès à ChatGPT, mais pas à ce texte, perdrait-il quelque chose ? Lister ce que le texte apporte qu'une IA ne pourrait pas produire seule (données propres, cas vécus, positions). Si la liste est vide ou presque, le dire franchement en tête de la partie 3 : le problème n'est alors pas le style, c'est le fond.

## Adapter au format

- **Texte court (post, newsletter de moins de 300 mots)** : les règles 3, 9, 11 et 12 s'appliquent avec souplesse, il n'y a souvent qu'une section. Les règles 1, 2, 5, 7, 10 et 13 restent pleinement valables.
- **Page de service ou de vente** : la règle 16 compte double. Une page qui commence par la présentation de l'entreprise perd le lecteur avant d'avoir parlé de son problème. Le garde-fou 6 aussi : ces pages vivent de leur référencement.
- **Texte déjà solide** : le dire dès le diagnostic et limiter les corrections à ce qui en a vraiment besoin. Un bon texte qui ressort presque intact est un bon résultat.
- **Texte dans une autre langue que le français** : appliquer les règles de rythme, de structure et de fond. Pour la règle 2, suivre les usages typographiques de la langue, mais signaler un emploi du tiret nettement plus fréquent que dans un texte écrit à la main.

## Déroulé

1. Lire le texte en entier une première fois sans rien corriger, pour en saisir l'intention, la voix et le mot-clé visé.
2. Passer les 18 règles une à une et noter chaque problème avec son extrait exact.
3. Relever les incohérences internes : un nombre annoncé qui ne correspond pas à ce qui suit (« cinq questions » suivies de quatre), des dates ou des chiffres qui se contredisent, un nom écrit de deux façons. Ne pas trancher : les signaler en partie 3.
4. Sauf en mode « diagnostic seul », réécrire en appliquant les corrections, dans le respect des garde-fous.
5. Contrôler la version corrigée avant de la rendre :
   - aucun tiret cadratin ou demi-cadratin en incise (chercher les caractères « — » et « – ») ;
   - au plus une formule ternaire, et aucune fausse opposition introduite par la réécriture ;
   - les trois derniers paragraphes n'ont rien de récapitulatif ;
   - le mot-clé principal est dans le titre et dans les 100 premiers mots ;
   - aucun fait nouveau n'a été introduit (comparer chiffres, noms et dates avec l'original) ;
   - chaque marqueur `[À COMPLÉTER]` figure dans la partie 3.

## Sortie

### 1. Diagnostic

En tête : le mot-clé principal retenu, puis un tableau, une ligne par problème trouvé, dans l'ordre du texte :

| N° | Règle | Extrait | Problème | Correction |
|---|---|---|---|---|

Puis une phrase de synthèse : les deux ou trois réflexes dominants du texte.

Si une règle est respectée, ne pas l'inscrire. Si le texte est déjà propre, le dire en une phrase plutôt que de chercher des problèmes.

### 2. Version corrigée

Le texte complet réécrit, en Markdown propre (titres, listes, gras conservés), avec les marqueurs `[À COMPLÉTER : …]` à leur place. Puis une ligne qui récapitule les contrôles de l'étape 5.

### 3. Matière à fournir par l'auteur

En tête, le verdict du test ChatGPT (règle 18). Puis :

- la liste des marqueurs `[À COMPLÉTER]`, chacun avec la question précise à poser à l'auteur pour obtenir la matière manquante (par exemple : « Avez-vous un client pour qui cette méthode n'a pas fonctionné ? Que s'est-il passé ? ») ;
- les incohérences relevées à l'étape 3, à trancher par l'auteur ;
- les autres points d'attention éventuels (typographie à harmoniser, mot-clé déplacé).

## Où rendre la sortie

- **Texte collé dans la conversation** : rendre la sortie dans la conversation. Présenter la version corrigée dans un bloc de code Markdown, pour qu'elle se copie telle quelle sans symboles parasites.
- **Fichier fourni en entrée** (et si l'environnement permet d'écrire des fichiers) : écrire la sortie dans un fichier `<nom-du-fichier>.relecture.md`, dans le même dossier que l'original. Si ce fichier existe déjà, ajouter la date : `<nom-du-fichier>.relecture-AAAA-MM-JJ.md`. Ne jamais modifier le fichier d'origine. Dans la conversation, donner seulement le chemin du fichier créé, la synthèse du diagnostic et le verdict du test ChatGPT.
- **Demande « en fichier » ou « en Markdown » pour un texte collé** : écrire `relecture-AAAA-MM-JJ.md` dans le dossier de travail.
- **Si l'environnement ne permet pas d'écrire de fichier** : rendre toute la sortie dans la conversation, dans un seul bloc de code Markdown, prête à être enregistrée.

Le fichier commence par un en-tête :

```yaml
---
type: relecture-anti-ia
date: AAAA-MM-JJ
source: "nom du fichier relu, ou « texte collé »"
mot_cle: "mot-clé principal retenu"
problemes: 0
test_chatgpt: "réussi" ou "insuffisant"
---
```

Puis les trois parties, sous les titres `## 1. Diagnostic`, `## 2. Version corrigée` et `## 3. Matière à fournir par l'auteur`.

## Exemple court

**Avant**

> À l'heure où le numérique transforme tous les secteurs, la boulangerie artisanale doit, elle aussi, se réinventer — et c'est là que tout se joue. Fraîcheur, authenticité, proximité : trois valeurs au cœur de notre démarche. En somme, choisir notre boulangerie, c'est choisir la qualité.

**Diagnostic résumé** : ouverture contextuelle (règle 1), tiret cadratin (règle 2), transition passe-partout (règle 7), triptyque décoratif (règle 6), conclusion qui résume (règle 12), aucune matière propre (règle 18).

**Après**

> [À COMPLÉTER : un fait concret qui distingue cette boulangerie artisanale, par exemple l'heure de la première fournée ou l'origine de la farine.] La fraîcheur et la proximité se prouvent : [À COMPLÉTER : la preuve concrète de chacune].

Le texte d'origine ne contenait aucune information propre. La version corrigée le rend visible au lieu de le maquiller : c'est le comportement attendu. Le mot-clé « boulangerie artisanale » reste dans l'ouverture.

**Matière à fournir** : « Qu'est-ce que vos clients citent quand ils expliquent pourquoi ils viennent chez vous plutôt qu'ailleurs ? »

---

*Méthode Do Ingenia, issue de la relecture des contenus produits pour nos clients. Plus de détails : [doingenia.com/skills](https://doingenia.com/skills/). Licence CC BY 4.0.*
