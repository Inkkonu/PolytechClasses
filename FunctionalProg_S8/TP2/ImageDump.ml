open Couleur
open Image


(* procedure *)
let output_myint chan f =
  output_char chan (Char.chr (norm f))


(* procedure *)
let output_pixel chan (r,v,b) =
  begin
    output_myint chan r ;
    output_myint chan v ;
    output_myint chan b ;
  end 
;;

let render_pixel = output_pixel stdout
;;


(* itérateur simulant une boucle *)
let rec repeat min max f =
  if min <= max
  then
    let _ = f min 
    in repeat (min+1) max f
  else ()


let output_line chan x y pas nb im = 
  repeat 0 (nb-1) (fun n -> output_pixel chan (im (x +. (float_of_int n)*.pas, y))) ;; 


let output_image chan rect (dimx, dimy) im =
  let pasx = (rect.maxx -. rect.minx) /. float_of_int dimx
  and pasy = (rect.maxy -. rect.miny) /. float_of_int dimy
  in
  repeat 0 (dimy - 1) (fun n -> output_line chan rect.minx (rect.miny +. (float_of_int n) *. pasy) pasx dimx im)

(* pure function *)
let ppm_header nbx nby = 
  "P6 " ^ (string_of_int nbx) ^ " " ^  (string_of_int nby) ^ " 255\n" ;;

(* procedure *)
let output_ppm_header chan (nbx, nby) = 
    output_string chan (ppm_header nbx nby)


let output_ppm chan rect out_size im =
  let _ =  output_ppm_header chan out_size 
  in
  output_image chan rect out_size (im:image)

   


let print_ppm = output_ppm stdout ;;


let write_ppm nom rect size im = 
  let c = open_out nom
  in  let _ = output_ppm c rect size im 
      in  close_out c
      
