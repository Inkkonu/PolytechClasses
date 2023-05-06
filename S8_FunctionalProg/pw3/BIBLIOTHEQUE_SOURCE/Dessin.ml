
open Sdlvideo;;
open Params;;
open Utils;;

type texture_id = GlTex.texture_id ;;
type surface_ecran = unit ;;


let draw_image (tid, tx, ty) (x,y)  = 
  let x1 = x +. tx
  and y1 = y +. ty
  in
  begin
    GlTex.bind_texture `texture_2d tid;
    GlDraw.begins `quads; 
    GlTex.coord2(0.0, 0.0) ; GlDraw.vertex2 (x,  y1) ;
    GlTex.coord2(0.0, 1.0) ; GlDraw.vertex2 (x,  y ) ;
    GlTex.coord2(1.0, 1.0) ; GlDraw.vertex2 (x1, y ) ;
    GlTex.coord2(1.0, 0.0) ; GlDraw.vertex2 (x1, y1) ; 
    GlDraw.ends ();
  end ;;

let draw_image_symH (tid, tx, ty) (x,y)  = 
  let x1 = x +. tx
  and y1 = y +. ty
  in
  begin
    GlTex.bind_texture `texture_2d tid;
    GlDraw.begins `quads; 
    GlTex.coord2(1.0, 0.0) ; GlDraw.vertex2 (x,  y1) ;
    GlTex.coord2(1.0, 1.0) ; GlDraw.vertex2 (x,  y ) ;
    GlTex.coord2(0.0, 1.0) ; GlDraw.vertex2 (x1, y ) ;
    GlTex.coord2(0.0, 0.0) ; GlDraw.vertex2 (x1, y1) ; 
    GlDraw.ends ();
  end ;;



