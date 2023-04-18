#pragma once
#include "BNode.h"

template<typename T>
class BNodeLeaf : BNode<T>
{
public:
	explicit BNodeLeaf(T v, unsigned char l) : BNode(v), letter(l) {}; // Constructeur par défaut
	BNodeLeaf(const BNodeLeaf&); // Constructeur de recopie
	BNodeLeaf(BNodeLeaf&&); // Constructeur de déplacement
	virtual ~BNodeLeaf(); // Destructeur éventuellement virtuel
	BNodeLeaf& operator=(const BNodeLeaf&); // Opérateur d’affectation
	BNodeLeaf& operator=(BNodeLeaf&&); // Opérateur de déplacement
private:
	unsigned char letter;
};

