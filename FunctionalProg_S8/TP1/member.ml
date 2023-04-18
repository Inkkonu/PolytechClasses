let rec member l x = match l with
	| [] -> false
	| h::t -> if x = h then true else member t x;;

let a = member [1;5;6;9] 9;;
