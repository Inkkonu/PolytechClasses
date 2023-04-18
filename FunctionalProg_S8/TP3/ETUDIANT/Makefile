BIBDIR = ../BIBLIOTHEQUE_DISTRIB
BIB = $(BIBDIR)/Interface

all: Squelette.play documentation

Squelette.play : Squelette.cmo $(BIB).cma
	ocamlc -I +sdl -I +lablGL -o $@ unix.cma bigarray.cma sdl.cma sdlloader.cma sdlmixer.cma lablgl.cma $(BIB).cma $<


Squelette.cmo: Squelette.ml $(BIB).cmi
	ocamlc -c -I $(BIBDIR) $<

.PHONY : documentation clean

doc:
	mkdir doc

documentation: doc
	ocamldoc -d doc -html -charset iso-8859-1 -I $(BIBDIR) *.ml 

clean:
	rm -f Squelette.cmo Squelette.cmi *~
