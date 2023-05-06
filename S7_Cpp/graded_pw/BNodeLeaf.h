#pragma once
#include "BNode.h"

template<typename T>
class BNodeLeaf : BNode<T>
{
public:
	explicit BNodeLeaf(T v, unsigned char l) : BNode(v), letter(l) {}; // Constructeur par d�faut
	BNodeLeaf(const BNodeLeaf&); // Constructeur de recopie
	BNodeLeaf(BNodeLeaf&&); // Constructeur de d�placement
	virtual ~BNodeLeaf(); // Destructeur �ventuellement virtuel
	BNodeLeaf& operator=(const BNodeLeaf&); // Op�rateur d�affectation
	BNodeLeaf& operator=(BNodeLeaf&&); // Op�rateur de d�placement
private:
	unsigned char letter;
};

