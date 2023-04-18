Bibliothèques nécessaires :

 * SDL (package libsdl-ocaml-dev sous Ubuntu, ocamlsdl sous opam)
 * lagblGL (package liblablgl-ocaml-dev sous Ubuntu, package lablgl sous opam)


INSTALLATION :
  Dans ce TP vous disposez d'une bibliothèque permettant d'afficher des sprites et de lire des actions au clavier pour un jeu vidéo. On considère que vous ne pouvez pas modifier cette bibliothèque, vous allez seulement l'utiliser. Sur Madoc la bibliothèque est donnée de manière à fonctionner sur les machines des salles de TP de Polytech. Ici, on vous donne les sources de la bibliothèque uniquement pour que vous puissiez la compiler pour votre machine personnelle. Suivez la marche à suivre ci-dessous pour la compiler avant de commencer à programmer, puis n'y touchez plus. 

1) Allez dans le répertoire BIBLIOTHEQUE_SOURCE puis faites 'make export'. Ceci compile la bibliothèque et l'installe dans le répertoire BIBLIOTHEQUE_DISTRIB.

2) Allez dans le répertoire ETUDIANT et faites 'make'. Ceci compile le fichier Squelette.ml qui s'appuie sur la bibliothèque compilée installée dans BIBLIOTHEQUE_DISTRIB.

3) Lancez l'exécutable créé Squelette.play et trouvez les touches du clavier qui sont utilisées (elles provoquent une variation de la sortie sur la console texte).

4) Vous pouvez commencer à travailler dans le fichier Squelette.ml

DOCUMENTATION :
   La documentation de la bibliothèque fournie est visible sous forme HTML dans le répertoire BIBLIOTHEQUE_DISTRIB. Elle a été générée à partir du code source à l'étape 1).
