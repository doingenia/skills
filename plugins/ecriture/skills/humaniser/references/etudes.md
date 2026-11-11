# Études qui fondent la skill `/humaniser`

Relevé du 11/11/2026. Chaque règle de la skill qui s'appuie sur un chiffre renvoie ici. Un chiffre
non retrouvé dans sa source est marqué comme tel et ne sert pas de règle.

Nos règles s'appuient sur ces mesures. Elles ne prouvent pas que la méthode marche : la seule preuve,
ce sont nos essais, publiés avec leurs textes dans `essais/` pour être rejoués.

---

## 1. Labbé, Labbé et Savoy (2024) : ChatGPT écrit les vœux des présidents

« ChatGPT as speechwriter for the French presidents », arXiv 2411.18382. Lu en entier.

**Protocole** : vœux du 31 décembre de Chirac, Sarkozy, Hollande et Macron ; pour chaque discours,
ChatGPT reçoit le vrai texte comme modèle et écrit le sien. Textes lemmatisés et comparés catégorie
par catégorie. Seule étude chiffrée trouvée sur le style d'une IA en français. Limites : un genre
(discours oral écrit), une version de ChatGPT non précisée (2023-2024), des textes générés courts
(souvent moins de 1 000 mots).

**Longueur des phrases (tableau 10)**

| | Présidents | ChatGPT |
|---|---|---|
| Mode (longueur la plus fréquente) | 13 mots | 19 mots |
| Médiane | 19,9 | 20,1 |
| Moyenne | 21,0 | 21,7 |
| Écart type | 16,4 | 10,9 |
| Coefficient de variation | 78 % | 50 % |
| 1er décile / 9e décile | 12,0 / 57,9 mots | 14,4 / 41,2 mots |
| Rapport D9 / D1 | 3,8 | 1,9 |

- La moyenne est la même : ce qui trahit le modèle est la **dispersion**, pas la longueur.
- ChatGPT surproduit les phrases de 15 à 39 mots et produit **moins** de phrases de moins de 15 mots
  et de plus de 39 mots. Il en produit moins, pas « presque aucune » (formule de samber, inexacte).
- Texte humain : mode < médiane < moyenne (distribution tirée vers les longues phrases). ChatGPT :
  les trois presque égales (distribution symétrique, « en cloche »).
- Lien proposé par les auteurs : moins de phrases très longues parce que moins de subordonnées.

**Mots (pour mille mots, écart en %)**

| Mot | Présidents | ChatGPT | Écart |
|---|---|---|---|
| également | 0,29 ‰ | 3,71 ‰ | + 1 178 % |
| défi | 0,52 ‰ | 4,14 ‰ | + 696 % |
| tenir | 1,07 ‰ | 2,76 ‰ | + 158 % |
| continuer | 1,10 ‰ | 2,69 ‰ | + 145 % |
| devoir | 3,62 ‰ | 7,27 ‰ | + 101 % |
| nous | 16,10 ‰ | 24,28 ‰ | + 51 % |
| falloir | 1,00 ‰ | 0,07 ‰ | − 93 % |
| on | 0,84 ‰ | 0,07 ‰ | − 92 % |
| dire | | | − 78 % |

- Catégories : ChatGPT emploie plus de noms (+ 7 %), d'adjectifs (+ 13 %), de déterminants
  possessifs, de nombres ; 22 % de pronoms en moins, moins de subordonnées, des temps simples
  (présent, participe passé).
- « défi » vient en formules figées : « relever les défis », « face aux défis ».
- Avec un court texte en exemple, ChatGPT imite assez bien un message court : donner un échantillon
  de voix aide.

**Ce qu'on en tire** : règles de rythme chiffrées (étape 3bis), « également » et « défi » en tête du
lexique, « on » et « il faut » à réintroduire quand le registre le permet, méfiance envers les noms
en série et les possessifs.

---

## 2. Reinhart et al. (2025) : les LLM écrivent-ils comme des humains ?

PNAS, vol. 122, doi 10.1073/pnas.2422455122 ; arXiv 2410.16107. Anglais seulement. Chaque modèle
reçoit le début d'un texte humain et écrit la suite ; on compare avec la vraie suite, sur les traits
grammaticaux de Biber.

| Trait (GPT-4o face aux humains) | Rapport |
|---|---|
| Propositions au participe présent | × 5,3 |
| Propositions « that » en sujet | × 2,6 |
| Nominalisations | × 2,1 |
| Coordination de groupes (« X et Y ») | × 1,9 |
| Passif sans agent | × 0,5 |
| Mots comme « tapestry », « camaraderie » | plus de × 100 |

- Les modèles de base (non réglés pour la conversation) écrivent presque comme les humains ; l'écart
  vient du **réglage par instructions**.
- Les classifieurs séparent humains et modèles réglés à 93-98 %.

**Ce qu'on en tire** : le participe présent (C4) et les nominalisations (« la mise en place de »,
« la réalisation de ») sont parmi les marques les plus sûres ; les paires « X et Y » en série
aussi (B1, D5). Le passif sans agent n'est pas un défaut d'IA : on ne le chasse pas par principe.

---

## 3. Zanotto et Aroyehun (2025) : profils linguistiques humains et machines

EMNLP 2025, arXiv 2507.13614. Anglais, 8 domaines, 11 modèles, 467 985 textes.

- Les textes humains **varient davantage** que ceux des machines, d'un texte à l'autre et d'un
  domaine à l'autre.
- Les modèles récents se ressemblent de plus en plus entre eux (homogénéisation).
- GPT-4 est proche des humains sur la profondeur syntaxique et la longueur des phrases (18 à 19 mots
  contre 23,5) : la longueur moyenne ne trahit plus un modèle récent.
- Signes d'un auteur humain retenus par le classifieur : syntaxe plus simple, moindre similarité
  sémantique d'une phrase à l'autre.

**Ce qu'on en tire** : viser la variation (de longueur, de structure, d'un paragraphe à l'autre),
jamais une moyenne.

---

## 4. Kobak et al. (2025) : le vocabulaire en excès des résumés scientifiques

Science Advances, doi 10.1126/sciadv.adt3813 ; arXiv 2406.07016. Plus de 15 millions de résumés
PubMed, 2010-2024.

- Méthode : repérer les mots dont la fréquence bondit après l'arrivée des modèles (« delves »,
  « showcasing », « crucial », « pivotal »).
- Au moins 13,5 % des résumés de 2024 passés par un modèle, jusqu'à 40 % dans certains sous-ensembles.

**Ce qu'on en tire** : la méthode de mesure du vocabulaire en excès, et la preuve que ces listes
vieillissent vite.

---

## 5. Études françaises sur la détection

- Antoun et al., TALN 2023 : les détecteurs repèrent ChatGPT dans le domaine d'entraînement, mais
  échouent hors domaine.
- Liyanage et Buscaldi, TALN 2023 (textes académiques) : plus le corpus est réaliste, plus la
  détection est difficile.
- Alavoine et al., JEP-TALN 2024 : les textes de ChatGPT partagent des traits, mais des lecteurs
  humains ne les identifient pas clairement.

**Ce qu'on en tire** : confirme le choix de ne pas faire deviner l'origine d'un texte à la skill
(règle 7).

---

## 6. Chiffres non retrouvés

- « 16 % des erreurs de ChatGPT en français sont d'origine anglaise » (samber) : le seul chiffre
  approchant (environ 16 % des annotations liées à l'anglais) vient d'une étude HumEval 2024
  (aclanthology 2024.humeval-1.2) sur plusieurs modèles, pas lue en entier. Ne pas citer tel quel.
- « notamment : 1 pour 200 mots chez l'IA contre 1 pour 800 chez l'humain » (samber) : source non
  trouvée.

---

## À lire ensuite

- HumEval 2024 (2024.humeval-1.2) : erreurs des modèles en français et influence de l'anglais.
- Mercanti-Guérin, The Conversation (2026), avec la DGLFLF : « Comment dé-IA-iser nos écrits ».
  Qualitatif ; renvoie à des études sur l'uniformisation des textes de marque.
- Benchmark de variation stylistique, arXiv 2509.10179.
