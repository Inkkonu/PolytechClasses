open Image
open ImageDump
open Lueur

(* Utiliser ce fichier pour appeler et tester vos fonctions. *)


(* Test 1 *)
let _ = print_ppm  { minx = 0.0 ; maxx = 500.0 ; miny =  0.0 ; maxy = 500.0} (500,500) (lueur (255,0,0) (250.,250.)) ;; 

