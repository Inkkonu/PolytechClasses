(** Module d'IHM *)




(** {2 Initialisation }*)

(** La définition du type [screen] est volontairement masquée. *)
type image = Init.texture_id
type screen = {
  vaisseau : image * float * float ; 
  missile  : image * float * float ;
  ennemi   : image * float * float ;
  fond     : image * float * float ;
}


(** On doit appeler la fonction d'initialisation [init] pour obtenir une valeur du type [screen]. *)


let configure_evenements () =
  begin
(* On active uniquement les evenements qu'on sait traiter *)
    Sdlevent.disable_events Sdlevent.all_events_mask;
    Sdlevent.set_state true Sdlevent.QUIT_EVENT ;
    Sdlevent.set_state true Sdlevent.KEYDOWN_EVENT ;
  end

let init () = 
  begin
    Init.init_fenetre () ;
    Init.init_systeme_dessin() ;
    configure_evenements () ;
    let i = Init.load_texture true "ressources/Spaceship_sprite_1.png"
    and m = Init.load_texture true "ressources/missile.png"
    and e = Init.load_texture true "ressources/ennemi.png"
    and f = Init.load_texture false "ressources/clouds2.png"
    in { vaisseau = (i, 128.0, 32.0); 
	 missile = (m, 64.0, 32.0);
	 ennemi = (e, 64.0, 64.0) ;
	 fond = (f, Params.largeur_fenetre_f , Params.hauteur_fenetre_f) ;
}
  end

(** {b Question :} D'un point de vue génie logiciel, quelle est l'utilité de forcer l'usage d'un paramètre de type [screen] dans les fonctions d'affichage ci-dessous ? *)



(** {2 Disctinction des joueurs } *)

(** Le type [joueur] sert à distinguer les deux joueurs. *)
type joueur = A | B  


(** {2 Positions écran } Description de l'écran et des positions à l'écran. *)

type position = int * int

let largeur_fenetre = Params.largeur_fenetre
let hauteur_fenetre = Params.hauteur_fenetre




(** {2 Sprites} Types de données décrivant les différents sprites. *)

type ennemi = Projectile | Vaisseau | Boss of int
type tir = Balle | Laser of int

let get_size_of_ennemi e =
  match e with
  | Projectile -> (54,26)                                            (* FIXME *)
  | Vaisseau -> (46,46)
let get_size_of_tir    t = (8,8)                                     (* FIXME *)
let size_of_vaisseau = (96,30)

(** {2 Affichage } Fonctions d'affichage. *)

let floatpos (x,y) = (float_of_int x, float_of_int y)
let zeropos = (0.0, 0.0)

let affiche_vaisseau s j p = Dessin.draw_image s.vaisseau (floatpos p)
let affiche_ennemi   s e p = 
  let dessin = 
    match e with
    | Projectile -> s.missile
    | Vaisseau -> s.ennemi                                             (* FIXME *)
  in  Dessin.draw_image dessin (floatpos p)            


let affiche_tir       s t p = Dessin.draw_image_symH s.missile (floatpos p) (* FIXME *)


let flip s = 
  begin
    Sdltimer.delay 10 (* uniquement pour les machines mal configurées sur lesquelles le flip est instantané *) ;
    Init.flip() ;
    Dessin.draw_image s.fond zeropos                        (* FIXME : fond *)
  end


(** {2 Actions joueur } Actions lues sur le clavier. *)
  

type action_instantanee =  QuitAction | Continue of joueur option

(* Les tirs sont déclenchés uniquement lorsque la touche devient enfoncée.
   Les déplacements sont actifs tant que la touche reste enfoncée.          *)
let rec traite_evenements () = 
  match Sdlevent.poll () with
    None -> Continue None
  | Some (Sdlevent.QUIT) -> QuitAction
  | Some (Sdlevent.KEYDOWN k) -> 
     (
      match k.Sdlevent.keysym with
      | Sdlkey.KEY_ESCAPE -> QuitAction 
      | Sdlkey.KEY_SPACE -> Continue (Some A)
      | Sdlkey.KEY_RCTRL -> Continue (Some B)
      | Sdlkey.KEY_RETURN -> Continue (Some B)
      | _ -> Continue None
    )

  | Some _ -> failwith "evenement non reconnu"
;;


let int_z = Sdlkey.int_of_key Sdlkey.KEY_z ;;
let int_q = Sdlkey.int_of_key Sdlkey.KEY_q ;;
let int_s = Sdlkey.int_of_key Sdlkey.KEY_s ;;
let int_d = Sdlkey.int_of_key Sdlkey.KEY_d ;;
let int_up = Sdlkey.int_of_key Sdlkey.KEY_UP ;;
let int_down = Sdlkey.int_of_key Sdlkey.KEY_DOWN ;;
let int_left = Sdlkey.int_of_key Sdlkey.KEY_LEFT ;;
let int_right = Sdlkey.int_of_key Sdlkey.KEY_RIGHT ;;

let pushed st k =  Bigarray.Array1.get st k <> 0


type v_direction = Up | Down
type h_direction = Left | Right
type shoot = bool

type commande_joueur = (v_direction option * h_direction option * shoot)

type commande_jeu = QuitCommand | NormalCommand of commande_joueur * commande_joueur



(* Les tirs sont déclenchés uniquement lorsque la touche devient enfoncée.
   Les déplacements sont actifs tant que la touche reste enfoncée.          *)
let get_actions () =
  match traite_evenements () with
  | QuitAction -> QuitCommand
  | Continue a ->
     let (b1,b2) = match a with 
       | Some A -> (true,false)
       | Some B -> (false,true)
       | None -> (false, false)
                   
     and state = Sdlkey.get_key_state ()

     in
     
     let v1 =
       if pushed state int_z 
       then Some Up
       else 
         if pushed state int_s
         then Some Down
         else None
     and v2 = 
       if pushed state int_up 
       then Some Up
       else 
         if pushed state int_down
         then Some Down
         else None
     and h1 =
       if pushed state int_q 
       then Some Left
       else 
         if pushed state int_d
         then Some Right
         else None
     and h2 = 
       if pushed state int_left 
       then Some Left
       else 
      if pushed state int_right
      then Some Right
      else None
     in
     NormalCommand ((v1, h1, b1), (v2, h2,  b2)) 

