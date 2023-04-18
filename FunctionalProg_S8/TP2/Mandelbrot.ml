
let trop_grand (x,y) = (x*.x) +. (y *. y) > 4.0  ;;
let suivant (a,b) (x,y) = (x *. x -. y *. y +. a, 2.0 *. x *. y +. b) 

type result = Diverge of int | MaxIter

let rec mandelbrot_aux (a,b) point  maxiter =
  if trop_grand point
  then Diverge maxiter
  else 
    if  maxiter <= 0
    then MaxIter
    else     
      let nouveau_point = suivant (a,b) point
      in 
      mandelbrot_aux (a,b) nouveau_point (maxiter-1)

let mandelbrot nbmax (a,b)  = mandelbrot_aux (a,b) (0.0, 0.0) nbmax
  


