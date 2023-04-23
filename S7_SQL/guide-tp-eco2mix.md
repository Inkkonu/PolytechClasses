## Préambule

- jeu de données : éco2mix régionales consolidées et définitives disponibles sur le [portail ORE](opendata.reseaux-energies.fr)
- outils : SQL, duckdb, Python notebook

**Livrable** : un notebook dans lequel figurent des cellules de texte (markdown) entremêlées aux cellules de traitement (sql/python). La documentation (partie textuelle/graphique, commentaires du code) doit être abondante et particulièrement soignée.


## 1. Chargement et nettoyage des données

Préparer le jeu de données pour l'analyse.

Parmi les tâches attendues :

- Suppression des attributs inutiles (un seul champ temporel "Date - Heure" par exemple), incorrects et/ou grossièrement incomplet
- Vérification de la "TimeZone" pour le champ temporel
- Vérification / adaptation des types dans chaque colonne
- Traitement éventuel des valeurs à null
- Consolidation (recalcul) du TCO
- Ajout d'une colonne pour le total de production instantanée 

En fonction de vos besoins, il est possible de compléter cette liste avec d'autres pré-traitements. Il est impératif de documenter chaque traitement.

## 2. Exploration

Construire les requêtes SQL suivantes, avec éventuellement un rendu visuel (graphique). Tout "embellissement" du résultat (dans la mesure où il améliore effectivement la lisibilité du résultat) sera apprécié.

Le résultat de chaque requête doit faire l'objet d'une brève interprétation. Si nécessaire, un complément d'investigation (une ou plusieurs requêtes supplémentaires, qui permettent une interprétation plus fine) peut être proposée pour approfondir un sujet.

1. **Groupement et agrégation simples** : Production (en GWh) et consommation (en GWh), ainsi que leurs versions min, max et moyenne instantanées (en Mw), par mois et par région.
2. **Pivot** (construction `CASE WHEN`) : construire une table (résultat de requête) de la consommation (GWh) journalière montrant une colonne par région. Incidemment, chaque date devient une clé de la relation. Autrement dit, il y a une ligne de données de consommation pour chaque date.
3. **Fenêtre glissante** (*window function* avec `RANGE`) : la consommation (GWh) du mois écoulé, chaque jour.
4. **Variation** (*window function*, avec *CTE* pour décomposer le calcul) : les 20 plus grands écarts de consommation quotidienne (GWh), d'un jour à l'autre.
5. **Quantité cumulée** (*window functions* + *CTE*) : jour du dépassement des énergies renouvelables, pour chaque année (de 2013 à 2021). En d'autres termes, à quel moment de l'année (une date) la consommation atteint -dépassse- la production annuelle totale des filières renouvelables ?
6. **Calcul de point fixe** (*CTE récursive*) : trouver toutes les périodes correspondant aux 3 plus longues séquences d'augmentation de la consommation instantannée. Voici un extrait (la première ligne) de résultat :

| Date - Heure | Durée (hh:mm:ss) | 	Région    | Séquence (MW*) | Rang |
| :----------- | :---             | ---       | ---             | --- |
| 2016-07-18 02:30:00	| 11:00:00	| Île-de-France| [4616, 4646, 4661, 4715, 4942, 5009, 5391, 568...| 1 |

7. **Construction du cube** (`GROUP BY CUBE|GROUPING SETS|ROLLUP`) : donner toutes les valeurs de consommation (en GWh) agrégés par jour, par mois, par année et sur toute la période, ainsi que par région, par zone (NO, NE, SO, SE et IdF) et sur l'ensemble du territoire métropolitain (à l'exclusion de la Corse, non représentée dans le jeu de données). Toutes les combinaisons de ces 2 dimensions (temps et géographie) doivent figurer dans le résultat.


## 3. De la zone de transit vers l'entrepôt

1. Intégrer un second jeu de données d'historique des températures, disponible sur le 
[portail opendatasoft](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm).
Résoudre les problèmes d'alignement, sur la base d'un relevé par jour. Conserver les températures minimale, maximale et moyenne.

2. Concevoir, implémenter et alimenter avec les données existantes, une base de données multidimensionnelle comportant les mesures Conso régionale quotidienne, Prod. régionale quotidienne par type d'énergie, sur les dimension : temps (jour, mois, saison, année, toute la période), géographie (région, quarts, pays), température (au degré, par intervalle (froid, tempéré, chaud, etc.), et toutes températures confondues).

3. Proposer (décrire) une procédure pour la mise-à-jour incrémentale (sans recalculer l'intégralité) de l'entrepôt lorsque de nouvelles données sont disponibles, en considérant notamment le changement de statut des *données consolidées* vers des *données définitives*.