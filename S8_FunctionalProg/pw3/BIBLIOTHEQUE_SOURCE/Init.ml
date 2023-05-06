open Sdlvideo;;
open Params;;

(* ----------------------- VIDEO ------------------*)

type surface_ecran = unit
type texture_id = GlTex.texture_id

let init_fenetre () =
  begin
    Sdl.init [`VIDEO ];
    Sdlgl.set_attr [ Sdlgl.DOUBLEBUFFER true] ; (* ?? *)
    Sdlmouse.show_cursor false;
    let _ = Sdlvideo.set_video_mode   ~w:largeur_fenetre   ~h:hauteur_fenetre  [`OPENGL] in
    () (* on ne renvoit pas la fenetre car OPENGL ne l'utilise pas comme parametre *)
  end

let init_systeme_dessin () = 
  begin    
    GlDraw.viewport 0 0 largeur_fenetre hauteur_fenetre;
    (*load_textures();
    load_bg_textures() ;*)
    Gl.enable (`texture_2d);
    GlClear.color (0.5, 0.5, 0.5);
    Gl.disable `depth_test;
    GlMat.mode(`projection);
    GlMat.load_identity ();
    GlMat.ortho (0., largeur_fenetre_f) (0., hauteur_fenetre_f) (-10., 10.) ;
    GlMat.mode `modelview;

    Gl.enable `blend;
    GlFunc.blend_func GlFunc.(`src_alpha)  GlFunc.(`one_minus_src_alpha); 
        
  end


(* ---- textures initialisation (after GL initialisation)  --- *)

let load_texture transp fic = 
  let s1 = Sdlloader.load_image fic in
  let (w, h, _) = Sdlvideo.surface_dims s1 in
  let pix1 = GlPix.of_raw (Sdlgl.to_raw s1) ~format:(if transp then `rgba else `rgb) ~width:w ~height:h in

  let tid = GlTex.gen_texture () in
  GlTex.bind_texture `texture_2d tid;

  GlTex.parameter `texture_2d (`mag_filter `nearest); (* scale when image bigger than texture*)
  GlTex.parameter `texture_2d (`min_filter `nearest); (* scale when image smalled than texture*)
  GlTex.image2d ~proxy:false ~level:0 ~internal:4 ~border:false pix1 ;
  tid
  
;;



let flip() = Sdlgl.swap_buffers () ;;


(* ---------- TERMINAISON ----------------------------------- *)


let quitte() =
  begin
    Sdl.quit();
    exit (-1);
  end
;;

(* ---------- ERREURS OPENGL ----------------------------------- *)

let check_video_error() =
  try Gl.raise_error "toto" 
  with e -> 
    begin 
      print_endline "erreur OPENGL" ; 
      Sdl.quit();
      raise e 
    end
