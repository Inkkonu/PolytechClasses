(** Le type des résultats *)
type result = 
  | Diverge of int 
  | MaxIter


(** fonction qui détermine si un point est dans l'ensemble de Mandelbrot. 
    Le premier argument est la précision du calcul. *)
val mandelbrot : int -> float * float -> result
