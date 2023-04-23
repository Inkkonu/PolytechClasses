
(* 3ds : 320X240 psp :480x272 *)

let largeur_fenetre = 480
and hauteur_fenetre = 272


let largeur_fenetre_f = float_of_int largeur_fenetre
and hauteur_fenetre_f = float_of_int hauteur_fenetre



(* --- command line options --- *)
let _ =
  Arg.parse [
  ] (fun _->()) "Pas d'options pour ce jeu ";;
