TARGET_DIRECTORY = ../BIBLIOTHEQUE_DISTRIB

all: export

Dessin.cmo : Dessin.ml Params.cmo Utils.cmo
	ocamlc  -I +sdl -I +lablGL -c -o $@ $<

Init.cmo : Init.ml Params.cmo 
	ocamlc  -I +sdl -I +lablGL -c -o $@ $<


Interface.cmo : Interface.ml Interface.cmi Dessin.cmi
	ocamlc -I +sdl -c $<

Interface.cmi : Interface.mli
	ocamlc -c $<

Params.cmo: Params.ml
	ocamlc -c $<
Utils.cmo: Utils.ml
	ocamlc -I +sdl -I +lablGL -c $<

.PHONY : documentation copy export clean

doc:
	mkdir doc


documentation: doc
	ocamldoc -d doc -html -charset iso-8859-1 Interface.mli 


Interface.cma: Params.cmo Utils.cmo Dessin.cmo Init.cmo Interface.cmo 
	ocamlc -I +sdl -I +lablGL -a $^ -o $@

export:  Interface.cma Interface.cmi documentation
	mkdir -p $(TARGET_DIRECTORY)
	cp Interface.cma $(TARGET_DIRECTORY)
	cp Interface.cmi $(TARGET_DIRECTORY)
	cp -r doc $(TARGET_DIRECTORY)

clean:
	rm -f *~ *.cmo Dessin.cmi Init.cmi Utils.cmi Params.cmi

