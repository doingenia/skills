# optimisation-geo

**Optimisation GEO : rendez vos articles citables par les IA.** Donnez un article, en ligne ou encore brouillon : le skill relève ce qui manque à sa forme pour qu'une IA puisse en reprendre un passage, et l'ajoute en surligné, à partir de ce que l'article dit déjà. Il sert le SEO et GEO aussi bien que le référencement IA.

Il ne réécrit aucune phrase, n'ajoute aucun fait, et un script contrôle le résultat mot pour mot.

## Installation

Dans Claude Code :

```
/plugin marketplace add doingenia/skills
/plugin install doingenia-geo@doingenia-skills
```

Ou, avec tout outil compatible avec les Agent Skills :

```
npx skills add doingenia/skills
```

Dans Mistral Vibe, copiez ce dossier dans `~/.vibe/skills/` (voir le [README du dépôt](../../../../README.md#installation)).

Aucune clé d'API ni compte n'est nécessaire. Le skill utilise la recherche web de l'outil qui l'exécute et deux scripts Python, sans dépendance : il faut donc un outil qui peut lancer Python et écrire des fichiers. Sans cela, il donne les ajouts à insérer et indique que le contrôle n'a pas été fait.

## Utilisation

Donnez une adresse, un fichier ou un texte collé :

```
Rends cet article citable par les IA : https://exemple.fr/blog/mon-article
```

Ou, dans Claude Code, lancez-le comme une commande (tapez `/optimisation` et laissez l'autocomplétion faire le reste) :

```
/doingenia-geo:optimisation-geo @article.md intention : informative
```

Testé avec Claude Code, sur des URL et des fichiers, et dans Mistral Vibe, sur un fichier.

Lancé sans article, le skill affiche son aide. Pour l'afficher à tout moment : `optimisation-geo aide`.

## Options

À écrire en langage courant dans votre demande.

| Ce que vous écrivez | Effet |
|---|---|
| `questions : …` | Vos questions réelles pour la FAQ (clients, support, Search Console). Sinon, le skill les cherche sur le web. |
| `intention : commerciale` ou `informative` | Sert à juger si la page est ancienne. Sinon, elle est déduite. |
| `diagnostic seul` | Le relevé, les propositions et les signalements, sans ajout. |
| `en fichier` | Le diagnostic est aussi écrit dans un fichier `.md`. |

## Ce que vous obtenez

1. **Un relevé de la forme** : résumé en tête, tableau, FAQ, H2 en question, titre, sources. Si tout y est, le skill dit qu'il n'y a rien à ajouter.
2. **Des ajouts surlignés** `==…==`, seulement s'ils manquent et si le contenu s'y prête : un résumé `**En bref** : …`, un tableau tiré des données de l'article, une FAQ de questions réelles auxquelles l'article répond déjà. Ils sont limités à 20 % des mots de l'article.
3. **Des propositions, non appliquées** : un titre, des H2 en question, les sources à trouver.
4. **Des signalements, sans réécriture** : passages vagues sans nom propre ni chiffre, sections qui commencent par « Il » ou « Cela » et ne se comprennent pas seules, page ancienne selon l'intention de recherche, années dépassées.
5. **Le résultat du contrôle.** Hors surlignage, chaque phrase et chaque titre doivent être identiques à l'original, accents compris. En cas d'échec, le skill le dit et ne livre pas l'article comme réussi.

L'article avec ajouts est écrit dans `<nom>.optimisation-geo.md`, à côté de `<nom>.original.md`. Votre fichier et votre page en ligne ne sont jamais modifiés. Vous relisez, puis retirez les `==`.

## D'où viennent les questions de la FAQ

De vous, ou d'une recherche web faite pendant l'exécution, avec le lien de chaque question. Une question non trouvée ne s'invente pas : sans questions réelles, pas de FAQ. La recherche porte sur le sujet, jamais sur des passages de votre brouillon.

## Ce que disent les études

Ces éléments sont plus fréquents sur les pages citées. Ce sont des **corrélations**, pas des causes.

Dans l'[étude de SISTRIX](https://www.sistrix.com/blog/citation-worthiness-study/) (96 418 pages en Allemagne, Autriche et Suisse, citées ou non, comparées à l'intérieur d'un même domaine), une page avec un tableau à ligne d'en-tête est citée 1,5 fois plus souvent, une page avec au moins une question en H2 1,4 fois, une page avec un résumé en tête 1,3 fois. L'étude met elle-même en garde contre les ajouts artificiels, et le facteur de la FAQ (1,5) porte sur le balisage FAQPage, à poser à la publication.

Le détail, les liens et les limites de chaque étude sont dans [references/etudes.md](references/etudes.md).

## Ce que le skill ne fait pas

- **Il ne promet aucune citation.** Il rend un article citable, ce qui ne veut pas dire cité.
- **Il ne réécrit rien.** Aucune phrase, aucun titre, même pour une faute : il la signale.
- **Il n'ajoute aucun fait.** Le contrôle refuse tout nombre absent de l'article. Ce qui manque au fond est signalé, à vous de l'apporter.
- **Il ne publie rien** et ne pose pas de données structurées.
- **Il ne mesure pas** ce que les IA disent de vous.
- **Il ne couvre que le français** pour l'instant.

Le contrôle a ses limites : il vérifie que votre texte est intact et que les chiffres des ajouts viennent de l'article, pas que les ajouts sont justes. La relecture reste la vôtre.

## Versions

Voir [CHANGELOG.md](CHANGELOG.md).

---

Méthode [Do Ingenia](https://doingenia.com), issue de notre travail sur les contenus. Textes sous licence [CC BY 4.0](../../../../LICENSE), scripts sous licence [MIT](../../../../LICENSE-CODE).
