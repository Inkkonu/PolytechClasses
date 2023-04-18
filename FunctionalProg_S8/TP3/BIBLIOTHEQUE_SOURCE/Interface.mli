(** Module d'IHM *)




(** {2 Initialisation }*)

(** La définition du type [screen] est volontairement masquée. *)
type screen


(** On doit appeler la fonction d'initialisation [init] pour obtenir une valeur du type [screen]. *)
val init : unit -> screen

(** {b Question :} D'un point de vue génie logiciel, quelle est l'utilité de forcer l'usage d'un paramètre de type [screen] dans les fonctions d'affichage ci-dessous ? *)



(** {2 Disctinction des joueurs } *)

(** Le type [joueur] sert à distinguer les deux joueurs. *)
type joueur = A | B  


(** {2 Positions écran } Description de l'écran et des positions à l'écran. *)

type position = int * int

val largeur_fenetre : int

val hauteur_fenetre : int

(** {2 Sprites} Types de données décrivant les différents sprites. *)

type ennemi = Projectile | Vaisseau | Boss of int
type tir = Balle | Laser of int

val get_size_of_ennemi : ennemi -> int * int
val get_size_of_tir    : tir    -> int * int
val size_of_vaisseau   : int * int

(** {2 Affichage } Fonctions d'affichage. *)

val affiche_vaisseau  : screen -> joueur -> position -> unit
val affiche_ennemi    : screen -> ennemi -> position -> unit
val affiche_tir       : screen -> tir    -> position -> unit

val flip : screen -> unit




(** {2 Actions joueur } Actions lues sur le clavier. *)

type v_direction = Up | Down
type h_direction = Left | Right
type shoot = bool
type commande_joueur = (v_direction option * h_direction option * shoot)

type commande_jeu = QuitCommand | NormalCommand of commande_joueur * commande_joueur



(** @raise Quit lorsque l'utilisateur veut quitter le jeu (touche Echap, ou signal reçu par le processus). *)
val get_actions : unit -> commande_jeu


