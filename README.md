# Skills Do Ingenia

[![Testé dans Claude Code](https://img.shields.io/badge/test%C3%A9%20dans-Claude%20Code-191919?logo=claude&logoColor=white)](#installation)
[![Testé dans Mistral Vibe](https://img.shields.io/badge/test%C3%A9%20dans-Mistral%20Vibe-FA520F?logo=mistralai&logoColor=white)](#installation)
[![Standard Agent Skills](https://img.shields.io/badge/standard-Agent%20Skills-0A66C2)](https://agentskills.io)

> **In English.** Agent skills for Claude and Mistral (Vibe), by Do Ingenia, a French SEO and GEO (Generative Engine Optimization) consultancy. They help experts turn tacit know-how into content that AI answer engines can cite, and measure what those engines say about a brand. Skills are written in French. Install instructions below work as is.

Les moteurs de réponse IA citent ce qu'ils ne peuvent pas inventer : le vécu terrain, les chiffres propriétaires, les cas réels. Ces skills pour Claude et Mistral servent à extraire cette expertise, à la rendre citable et à mesurer ce que les IA disent de vous.

Ce sont des méthodes que nous utilisons chez Do Ingenia avec nos clients, adaptées pour fonctionner seules.

## Installation

**Claude Code, sous forme de plugins** (une famille de skills par plugin) :

```
/plugin marketplace add doingenia/skills
/plugin install doingenia-ecriture@doingenia-skills
```

**Mistral Vibe** : copiez le dossier du skill dans `~/.vibe/skills/`, puis relancez Vibe :

```
git clone https://github.com/doingenia/skills.git
mkdir -p ~/.vibe/skills
cp -R skills/plugins/ecriture/skills/relecture-anti-ia ~/.vibe/skills/
```

**Tout outil compatible avec les Agent Skills** :

```
npx skills add doingenia/skills
```

## Les skills

| Famille | Plugin | Skill | Ce qu'il fait | Documentation |
|---|---|---|---|---|
| Écriture | `doingenia-ecriture` | [`relecture-anti-ia`](plugins/ecriture/skills/relecture-anti-ia/) | Relit un texte et retire les tics d'écriture qui trahissent une rédaction par IA, sans rien inventer. | [Mode d'emploi](plugins/ecriture/skills/relecture-anti-ia/README.md) |

D'autres familles arrivent : expertise (interview d'expert, capitalisation), GEO (perception des IA, citabilité d'une page). Le détail de chaque skill est sur [doingenia.com/nos-outils/skills](https://doingenia.com/nos-outils/skills/).

## La philosophie

**Architectes de vérité.** L'IA générative a fait tomber à zéro la valeur de l'information générique. Ce qui reste rare, et donc citable, c'est l'expertise humaine vérifiable. Nos skills partent de là : ils cherchent ce qu'une IA ne pourrait pas écrire seule, et refusent les généralités.

## Qui est derrière

[Do Ingenia](https://doingenia.com) est un cabinet de conseil SEO et GEO et d'ingénierie IA, basé à Sophia-Antipolis. Il a été fondé par [Denis Degioanni](https://www.linkedin.com/in/denisdegioanni/), qui travaille sur les technologies web depuis 1996.

## Contribuer

Les retours d'usage et les signalements de bugs sont les bienvenus dans les [issues](https://github.com/doingenia/skills/issues). Les pull requests sont acceptées pour les corrections. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

- **Textes des skills** (fichiers `SKILL.md` et documentation) : [CC BY 4.0](LICENSE). Vous pouvez les réutiliser et les adapter, y compris à des fins commerciales, en citant « Do Ingenia » avec un lien vers ce dépôt.
- **Scripts** : [MIT](LICENSE-CODE).

---

**Pour aller plus loin** : le détail des skills, des exemples et la façon dont nous les utilisons en mission sont sur [doingenia.com/nos-outils/skills](https://doingenia.com/nos-outils/skills/).
