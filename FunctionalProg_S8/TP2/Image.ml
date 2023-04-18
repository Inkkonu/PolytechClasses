open Couleur ;;


(** Type des images *)

type position = float * float
type image = position -> couleur



(** Exemples d'image *)

let im_black = (fun p -> (0, 0, 0))
let im_white = (fun p -> (255, 255, 255))

let rayures p = 
  match p with 
    | (x,y) -> (int_of_float (y) mod 255, int_of_float (x) mod 255, int_of_float (x +. y) mod 255)


(** Type des rectangles *)

type rectangle = { minx : float ; maxx : float ; miny : float ; maxy : float}
