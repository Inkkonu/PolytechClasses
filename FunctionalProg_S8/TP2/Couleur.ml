(** Type des couleurs. *)



type couleur = int * int * int  (** rouge, vert, bleu *)

(** Tous les entiers doivent être entre 0 et 255. *)



(** Fonctions utilitaires. *)


let norm n = min 255 (max 0 n)


let mult_teinte_float coeff (r,v,b) = (norm(int_of_float(coeff*.float_of_int(r))), norm(int_of_float(coeff*.float_of_int(v))), norm(int_of_float(coeff*.float_of_int(r))))