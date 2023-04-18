#pragma once
#include "BNode.h"

template<typename T>
class BNodeInter : BNode<T>
{
public:
	explicit BNodeInter(T v, BNode<T>& l, BNode<T>& r) : BNode(v), left(l), right(r) {}; // Constructeur par défaut
	BNodeInter(const BNodeInter&); // Constructeur de recopie
	BNodeInter(BNodeInter&&); // Constructeur de déplacement
	virtual ~BNodeInter(); // Destructeur éventuellement virtuel
	BNodeInter& operator=(const BNodeInter&); // Opérateur d’affectation
	BNodeInter& operator=(BNodeInter&&); // Opérateur de déplacement
private:
	BNode<T> left;
	BNode<T> right;
};

