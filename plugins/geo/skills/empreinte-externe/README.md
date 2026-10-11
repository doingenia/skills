# empreinte-externe

Quand ChatGPT se trompe sur votre entreprise, l'erreur vient souvent d'une fiche que vous avez oubliée : une ancienne page LinkedIn, une fiche Pappers, un homonyme sur Wikidata. Le skill relève ce que ces sources disent de vous, le compare à votre site et liste les écarts à corriger, du plus important au plus mineur. Vous savez ainsi quelle fiche corriger, fermer ou revendiquer.

Dans nos mesures, LinkedIn, Pappers et Wikipedia sont parmi les sources que les IA citent le plus.

La première version couvre les **entreprises françaises** (registre de l'État, SIREN).

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

Aucune clé d'API ni compte n'est nécessaire. Le skill utilise la recherche web et la lecture de pages de l'outil qui l'exécute.

Testé avec Claude Code et avec Mistral Vibe. Dans Vibe, indiquez le dossier `plugins/geo/skills` dans `skill_paths` (fichier `~/.vibe/config.toml`).

## Utilisation

Donnez le nom de l'entreprise et l'adresse de son site :

```
Relève l'empreinte externe de Maison Verdier Conseil, maisonverdier-exemple.fr
```

Ou, dans Claude Code, lancez-le comme une commande (tapez `/empreinte` et laissez l'autocomplétion faire le reste) :

```
/doingenia-geo:empreinte-externe Maison Verdier Conseil maisonverdier-exemple.fr en fichier
```

Le skill lit les mentions légales de votre site pour trouver le SIREN. S'il n'en trouve pas, ou si plusieurs sociétés apparaissent sans qu'on sache laquelle est visée, il s'arrête et vous le demande. Lancé sans argument, il affiche son aide. Pour l'afficher à tout moment : `empreinte-externe aide`.

## Options

À écrire en langage courant dans votre demande.

| Ce que vous écrivez | Effet |
|---|---|
| `siren : 123 456 789` | Impose le SIREN au lieu de le lire dans les mentions légales. |
| `réponses IA : …` | Collez ce qu'un assistant répond sur votre entreprise. Chaque erreur est rapprochée de l'écart qui l'explique. |
| `en fichier` ou `en Markdown` | Le relevé est écrit dans `<entreprise>.empreinte-externe.md`. |

## Ce que vous obtenez

1. **Un tableau des faits**, une colonne par source (site, registre, Pappers, LinkedIn, Wikidata et Wikipedia, fiche Google) : nom, SIREN, forme juridique, création, dirigeants, activité, siège, groupe.
2. **Les écarts à corriger**, numérotés du plus structurant au plus mineur. Un écart, c'est deux sources qui se contredisent sur un même fait, ou une entité confondue avec vous. Pour chacun : ce qui diffère, entre quelles sources, l'action (corriger, fermer, revendiquer, déclarer, créer) et où la faire. Le registre fait foi pour la création, la forme juridique et le siège. S'il n'y a aucun écart, le skill le dit.
3. **Les homonymes** qui risquent d'être confondus avec vous, et pourquoi : le même nom, ou un nom proche dans le même pays et le même secteur ou la même zone. Les sociétés de votre groupe sont signalées à part, comme une question.
4. **Les erreurs de l'IA rapprochées**, si vous avez collé des réponses. Le skill écrit « correspond mot pour mot » seulement quand c'est vérifiable, sinon « cohérent avec, non prouvé ».
5. **Les limites du relevé** : sources inaccessibles, LinkedIn et fiche Google vus partiellement.

## Sources consultées

Votre site (mentions légales, À propos, contact), le registre de l'État (API Recherche d'entreprises), Pappers (avec societe.com en repli quand Pappers est bloqué), LinkedIn, Wikidata, Wikipedia en français et la fiche Google telle que la recherche web la montre. Une source qui ne répond pas est notée dans le relevé, jamais passée sous silence.

## Ce que le skill ne fait pas

- **Il ne modifie rien.** Il propose, vous agissez : aucune fiche n'est éditée, aucun formulaire envoyé.
- **Il ne retient jamais un SIREN trouvé par une recherche sur le nom.** Une telle recherche ne remonte que des homonymes.
- **Il ne relève que l'empreinte professionnelle.** Pas de date de naissance ni d'adresse personnelle d'un dirigeant, même si une source les affiche.
- **Il n'invente rien.** Un fait introuvable s'écrit « non trouvé ». Il n'écrit que ce qu'une source du relevé établit.
- **Il ne donne pas de conseil de rédaction ni d'optimisation.** Pas de style typographique, pas de fiche Google à enrichir, pas de page Wikipedia à créer : il relève des désaccords entre sources.
- **Il ne couvre pas encore l'étranger.** Pour une entreprise immatriculée hors de France, il produit un relevé partiel, sans registre, et le dit.
- **Il montre d'où viennent les erreurs.** Il ne promet pas qu'une correction change la réponse d'une IA.

## Versions

Voir [CHANGELOG.md](CHANGELOG.md).

---

Méthode [Do Ingenia](https://doingenia.com), issue de notre travail avec des entreprises. Licence [CC BY 4.0](../../../../LICENSE).
