#pragma once
#include "BNodeInter.h"

template<typename T>
class BNode
{
public:
	explicit BNode(T v) : value(v) {};
	BNode(const BNode&); // Constructeur de recopie
	BNode(BNode&&); // Constructeur de déplacement
	virtual ~BNode(); // Destructeur éventuellement virtuel
	BNode& operator=(const BNode&); // Opérateur d’affectation
	BNode& operator=(BNode&&); // Opérateur de déplacement

	T GetValue() const { return value; };

private:
	T value;
};

template<typename T>
BNode<T> operator+(BNode<T> n1, BNode<T> n2) {
	BNodeInter<T> root = new BNodeInter(n1.value + n2.value, n1, n2);
	return root;
}


