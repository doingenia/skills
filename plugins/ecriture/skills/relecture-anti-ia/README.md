# relecture-anti-ia

Relit un texte en français et retire les tics d'écriture qui trahissent une rédaction par IA, **sans inventer de faits** et **sans perdre le mot-clé visé**.

Là où la matière manque (un cas vécu, une nuance, une position assumée), le skill ne comble pas le vide : il pose un marqueur `[À COMPLÉTER]` et vous dit quelle question vous poser.

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

## Utilisation

Collez votre texte :

```
Relis ce texte avec relecture-anti-ia :
[votre texte]
```

Ou donnez un fichier :

```
Relis @article.md avec relecture-anti-ia
```

Pour afficher les options dans Claude : `relecture-anti-ia aide`.

## Options

À écrire en langage courant dans votre demande.

| Ce que vous écrivez | Effet |
|---|---|
| `diagnostic seul` | Le tableau des problèmes, sans réécriture. |
| `en fichier` ou `en Markdown` | La sortie est écrite dans un fichier `.md`. Automatique quand vous fournissez un fichier. |
| `mot-clé : …` | Le mot-clé principal à protéger. Sinon, il est déduit du titre. |
| `c'est une page de service`, `c'est un post LinkedIn`… | Le type de texte. Sinon, il est déduit. |
| `pour des dirigeants de PME`… | Le public visé (facultatif). |

Exemple :

```
Relis @article.md avec relecture-anti-ia, diagnostic seul, mot-clé : traduction assermentée
```

## Ce que vous obtenez

1. **Un diagnostic** : un tableau, une ligne par problème (règle, extrait, problème, correction), puis les deux ou trois réflexes dominants du texte.
2. **Une version corrigée**, en Markdown, prête à copier.
3. **La matière à fournir** : le verdict du test ChatGPT (votre texte apporte-t-il quelque chose qu'une IA ne pourrait pas écrire seule ?), les questions à vous poser pour chaque marqueur `[À COMPLÉTER]`, et les incohérences relevées dans le texte.

Quand vous fournissez un fichier, la sortie est écrite dans `<nom-du-fichier>.relecture.md`, à côté de l'original. **L'original n'est jamais modifié.**

## Ce que le skill corrige

18 règles, regroupées en sept familles :

- **Ouverture** : les phrases qui posent un décor général au lieu d'entrer dans le sujet.
- **Typographie** : le tiret cadratin (—) en incise, rare en français écrit à la main.
- **Rythme et structure** : la symétrie mécanique, les phrases toutes de même longueur, les formules ternaires, les énumérations décoratives.
- **Transitions** : les liaisons passe-partout et les textes trop lisses.
- **Répétitions et tournures** : la formule martelée, la fausse opposition (« ce n'est pas X, c'est Y »).
- **Clôtures** : la punchline à chaque fin de section, la conclusion qui résume.
- **Incarnation et position** : l'absence de prise de position ou de nuance, les cas listés au lieu d'être racontés, la présentation d'entreprise en encart, les affirmations sans preuve.

Le détail de chaque règle est dans [SKILL.md](SKILL.md).

## Ce que le skill ne fait pas

- **Il n'invente rien** : ni cas client, ni chiffre, ni anecdote.
- **Il ne touche pas aux citations.**
- **Il ne réécrit pas votre voix** : votre vocabulaire et votre registre restent les vôtres.
- **Il ne rend pas un texte vide intéressant.** Si le fond manque, il vous le dit.

## Versions

Voir [CHANGELOG.md](CHANGELOG.md).

---

Méthode [Do Ingenia](https://doingenia.com), issue de la relecture des contenus produits pour nos clients. Licence [CC BY 4.0](../../../../LICENSE).
