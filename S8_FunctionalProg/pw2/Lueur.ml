open Couleur 
open Image

(* Vous pouvez coder ici vos fonctions pour créer des lueurs *)

let distance (x1,y1) (x2,y2) = sqrt((x1-.x2)*.(x1-.x2) +. (y1-.y2)*.(y1-.y2))

let lueur (r,v,b) (x1,y1) = (fun (x2,y2) -> mult_teinte_float (10./.distance (x1,y1) (x2,y2)) (r,v,b))