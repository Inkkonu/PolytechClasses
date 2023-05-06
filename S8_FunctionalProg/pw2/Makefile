FLAGS = -w a

a.out:  Couleur.cmo Image.cmo ImageDump.cmo Mandelbrot.cmo Lueur.cmo test.ml
	ocamlc $(FLAGS) -o $@ $^

Couleur.cmo : Couleur.ml Couleur.cmi
	ocamlc $(FLAGS) -c $<

Couleur.cmi : Couleur.mli
	ocamlc $(FLAGS) -c $<

Image.cmo : Image.ml Image.cmi Couleur.cmi
	ocamlc $(FLAGS) -c $<
Image.cmi : Image.mli Couleur.cmi
	ocamlc $(FLAGS) -c $<

Mandelbrot.cmi : Mandelbrot.mli
	ocamlc $(FLAGS) -c $<
Mandelbrot.cmo : Mandelbrot.ml Mandelbrot.cmi
	ocamlc $(FLAGS) -c $<

Lueur.cmo : Lueur.ml Couleur.cmi Image.cmi
	ocamlc $(FLAGS) -c $<



ImageDump.cmi: ImageDump.mli Image.cmi
	ocamlopt $(FLAGS) -c $<

ImageDump.cmo: ImageDump.ml ImageDump.cmi Image.cmi 
	ocamlc $(FLAGS) -c $<


clean:
	rm -f *.cmo *.cmi
mrproper:
	rm -f *.cmo *.cmi a.out

.PHONY : test

test : a.out
	./$< | display


