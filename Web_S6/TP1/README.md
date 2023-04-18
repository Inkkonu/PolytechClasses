# Compte-rendu de Killian Blain

## HTML

Rien de particulier à dire sur le HTML à part la div qui englobe les trois sections à gauche. Celle-ci me permet de
mettre l'aside de façon à peu près correcte car sinon, il dépassait et finissait en dessous du footer pour des
raisons obscures (pour moi).

## CSS

J'ai essayé de suivre le TP comme je pouvais donc peu de choses sortent de l'ordinaire à part peut-être quelques
éléments.

### Mise en page globale

Le main a _display: flex;_ car c'est ce qui me permet de mettre mon aside correctement car je lui ai enlevé la
position _absolute_ car cela me créait des problèmes :(\
La div a _padding-right: 10px;_ afin que ce ne soit pas collé à l'aside.

### Mise en page de l'entête

Je ne me suis pas embêté à cacher les liens des réseaux sociaux car ils ont disparu en mettant la hauteur du header à
70px.

_header ul:nth-child(2) {\
text-align: right;\
font-size: 80%;\
font-weight: normal;\
}_ \
Cela me permet de mettre le "Sign Up" et "Log In" à droite.

### Mise en page de la section Pop/Rock

Rien fait ici.

### Mise en page de la section Pop/Rock Artists Highlights

Envelopper l'image avec le nom du groupe dans un _article_ permet de les présenter alignées à l'horizontal.\
Je n'ai pas réussi à faire apparaître le texte par dessus l'image lorsque cette dernière était survolée. Elle devient
donc simplement grisée.


### Mise en page de la section Pop/Rock Song Highlights

Ici, malgré toutes mes tentatives, je n'ai pas réussi à mettre _More Pop/Rock Songs_ à droite alors que j'ai rajouté _text-align: right;_ dans _#popRockSongHighlights > a_.\
J'ai également pas réussi à mettre que la colonne Titre en bleu ou bien à faire afficher les bordures entre les lignes. J'ai dû faire une bêtise quelque part qui fait que ces modifications simples ne marchaient pas.

### Mise en page de l'aside Recent Pop/Rock Releases

Rien à dire ici à part que les _cite_ ne s'affichent pas à droite.

### Mise en page du footer

Rien à dire ici.

## Conclusion

La page manque beaucoup d'éléments pour le faire ressembler à ce qui était demandé car je n'y arrive tout simplement pas.