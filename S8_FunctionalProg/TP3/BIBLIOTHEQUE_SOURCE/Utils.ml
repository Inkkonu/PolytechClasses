let date_exacte () = Sdltimer.get_ticks () ;;

(* --- Durees --- *)
  
type  duree_im =  Im of int (* duree en nombre d'images *) 

and duree_tic = Tic of int ;;



      (* Le 20 vient du format MOD              *)
      (* (un tic toutes les 20 ms).             *)
      (* Le tempo est fixé dans le fichier MOD  *)


let im_of_tic ~tempo ~fps (Tic d) =
  let duree_tic = 20 * tempo
  in let date_miliseconds = duree_tic * d
     in let date_aux = int_of_float ((float_of_int date_miliseconds) *. fps) 
     in  Im (date_aux / 1000)  (* arrondi du a la division entiere pas grave *)



let im_par_sec nbim duree =  float_of_int (nbim* 1000) /. (float_of_int duree) ;;


let affiche_images_secondes nbim duree =
  (* duree en ms *)
  begin 
    print_float (im_par_sec  nbim duree) ;
    print_endline " images par seconde (moyenne)."
  end
;;



let affiche_score s =
  print_endline ("Score obtenu : " ^ (string_of_int s) ^ " points.");;

type erreur = Video | FichierAudio of string ;;

let show_err e = 
  let message = match e with
    | Video -> "Erreur video"
    | FichierAudio s -> "Fichier son " ^ s ^ " pas trouve."
  in prerr_string message
;;


type raison = Fin | Erreur of erreur ;;

exception Arret of raison ;;


let rec prefix f = function
  | [] -> []
  | e :: r when f e -> e :: (prefix f r)
  | _ -> [] 
;;

let rec remove_prefix f = function
  | [] -> []
  | e :: r when f e -> remove_prefix f r
  | r -> r 
;;
