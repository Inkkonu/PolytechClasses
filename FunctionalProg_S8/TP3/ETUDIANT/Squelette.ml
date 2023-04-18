open Interface ;;


type resultat = 
    Gagne of int 
  | Perdu of joueur * int
  | Interruption

(** IMPLEMENT-ME *)
let traite_collisions_tirs projectiles ennemis = (ennemis, projectiles, 0)

(** IMPLEMENT-ME *)
let traite_collision_joueurs j1 j2 ennemis = None

(** IMPLEMENT-ME *)
let traite_action (v_dir, h_dir,shoot) id info_j = 
  let _ =
    print_string (match id with 
    | A -> "J1 : "
    | B -> "J2 : "
    )
  in 
  let _ = 
    print_string (
      match v_dir with 
      | Some Up -> "U "
      | Some Down -> "D "
      | None -> "_ "
    )
  in let _ = 
       print_string (
	 match h_dir with
	 | Some Right -> "R "
	 | Some Left -> "L "
	 | None -> "_ "
    )
  in let _ = print_string (if shoot then "* " else "_ ")
       
     in ( (match id with A -> info_j + 1 | B -> info_j +2) mod hauteur_fenetre ,[]) 

(** IMPLEMENT-ME *)
let deplace_ennemis e proj = e

(** IMPLEMENT-ME *)
let affiche_jeu fen j1 j2 sc enn proj = 
  begin
    affiche_vaisseau fen A (j1,j1) ;
    affiche_vaisseau fen B (j2,j2) ;
    affiche_ennemi fen Vaisseau   (400,130) ;
    affiche_ennemi fen Projectile (320,150) ;
    affiche_tir fen Balle (20,150) ;
    flip fen
  end

let rec gestion fenetre j1 j2 ennemis projectiles score =

  (* On commence par lire le clavier *)
  match get_actions () with
  | QuitCommand -> Interruption
  | NormalCommand (action1,action2) ->

  (* On résoud les collisions des tirs avec les ennemis *)
  let (new_ennemis,new_projectiles,points) = traite_collisions_tirs projectiles ennemis
       
     in 
     let new_score = score + points
     in
     if new_ennemis = []
     then (Gagne new_score)
     else
       match traite_collision_joueurs j1 j2 ennemis
       with
       | Some j -> (Perdu (j, new_score))
       | None -> 
	  let (new_j1, projectiles_1) = traite_action action1 A j1 in
	  let (new_j2, projectiles_2) = traite_action action2 B j2 in
	  let _ = print_newline () in
	  let new_projectiles = projectiles_1 @ projectiles_2 @ new_projectiles in
	  let depl_ennemis = deplace_ennemis new_ennemis projectiles_2 in
	  
	  
	  let _ = affiche_jeu fenetre new_j1 new_j2 new_score depl_ennemis new_projectiles
	  in
	  
	  (* On finit par un appel récursif avec le nouvel état. *)
	  gestion fenetre new_j1 new_j2 depl_ennemis new_projectiles new_score

;;



(** Question : la fonction gestion est-elle implémentée par une récursion terminale? Pourquoi? *)

(** IMPLEMENT-ME *)
let init_j1 () = 10

(** IMPLEMENT-ME *)
let init_j2 () = 50

(** IMPLEMENT-ME *)
let init_ennemis () = [5]

let affiche_victoire s = 
  print_endline ("Congratulations. Your score is " ^ string_of_int s)

let affiche_defaite j s = 
  let perdant = match j with 
    | A -> "Player 1" 
    | B -> "Player 2"
  in 
  print_endline (perdant ^ " lose. Your score is " ^ string_of_int s)


(* Appel à la boucle de jeu. *)
let _ = 
  let s = init () 
  and j1 = init_j1 () 
  and j2 = init_j2 ()
  and ennemis = init_ennemis()
  in match gestion s j1 j2 ennemis [] 0
    with 
    | Perdu (j, s) ->
      affiche_defaite j s
      
    | Gagne s  ->
      affiche_victoire s
                       
    | Interruption -> print_endline ("Bye.")
;;
  
  
