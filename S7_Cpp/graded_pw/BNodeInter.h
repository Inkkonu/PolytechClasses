#pragma once
#include "BNode.h"

template<typename T>
class BNodeInter : BNode<T>
{
public:
	explicit BNodeInter(T v, BNode<T>& l, BNode<T>& r) : BNode(v), left(l), right(r) {}; // Constructeur par d�faut
	BNodeInter(const BNodeInter&); // Constructeur de recopie
	BNodeInter(BNodeInter&&); // Constructeur de d�placement
	virtual ~BNodeInter(); // Destructeur �ventuellement virtuel
	BNodeInter& operator=(const BNodeInter&); // Op�rateur d�affectation
	BNodeInter& operator=(BNodeInter&&); // Op�rateur de d�placement
private:
	BNode<T> left;
	BNode<T> right;
};

