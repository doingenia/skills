# humaniser : journal des versions

## 0.1.1

- Testé dans Mistral Vibe 3.1.2 (modèle GLM-5.3) : installation, appel par `/humaniser` et essai documentés.
- Exemple avant et après en tête du README.
- Exemple 1 corrigé : « rendement élevé » garde son adjectif.

## 0.1.0

- Première version publique, tirée de notre version interne : réécriture de la prose d'un texte français écrit par une IA, en une seule passe, sans changer ce qu'il dit.
- Option `--voix` : un guide de rédaction ou un texte humain de référence dont le skill reprend la voix.
- Contrôle des faits par ce à quoi ils se rapportent et par leurs nuances, pas seulement par leur présence.
- Structure (titre, intertitres, tableaux, FAQ) et précautions des secteurs réglementés intactes.
- Enchaînement avec `relecture-anti-ia` : relecture en diagnostic seul, l'auteur corrige son texte, puis humaniser ; un texte corrigé d'après ce diagnostic n'est pas un texte déjà humanisé, et les marqueurs `[À COMPLÉTER]` restent en place.
- Registre soutenu, institutionnel, juridique ou de santé tenu : ni « on » ni « il faut » réintroduits.
- Compte rendu : chaque passage cité est copié du fichier, jamais reconstitué de mémoire.
- Coquilles et fautes : renvoyées à une relecture orthographique, humaine ou avec un correcteur.
- Script `mesurer_rythme.py` : dispersion de la longueur des phrases avant et après. Cible : au moins 60 % de coefficient de variation, et jamais moins que l'original.
- Contrôle des faits étendu aux nombres écrits en lettres et à ceux des phrases d'annonce.
- Liste des tournures en neuf familles, exemples avant et après à l'échelle du paragraphe, études citées avec leurs limites.
- Jeu d'essais du comparatif avec blader/humanizer et samber humaniseur-fr (trois essais du 11/11/2026, le dernier sur cette version), à rejouer.
- Testé avec Claude Code.
