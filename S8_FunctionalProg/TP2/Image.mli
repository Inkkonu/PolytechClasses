
(** Type des images *)

type position = float * float
type image = position -> Couleur.couleur


(** Exemples d'images *)
val im_black : image
val rayures : image


(** Type des rectangles (pour cadrer une image lors de son affichage) *)

type rectangle = { minx : float; maxx : float; miny : float; maxy : float; }
