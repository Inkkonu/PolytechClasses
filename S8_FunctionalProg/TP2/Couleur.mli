(** Type des couleurs. *)

type couleur = int * int * int  (** rouge, vert, bleu, transparence *)

(** Tous les entiers doivent être entre 0 et 255. *)


val mult_teinte_float : float -> couleur -> couleur

(** Fonctions utilitaires. *)


val norm : int -> int



