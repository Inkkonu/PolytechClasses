#pragma once
#include "BNodeInter.h"

template<typename T>
class BNode
{
public:
	explicit BNode(T v) : value(v) {};
	BNode(const BNode&); // Constructeur de recopie
	BNode(BNode&&); // Constructeur de d�placement
	virtual ~BNode(); // Destructeur �ventuellement virtuel
	BNode& operator=(const BNode&); // Op�rateur d�affectation
	BNode& operator=(BNode&&); // Op�rateur de d�placement

	T GetValue() const { return value; };

private:
	T value;
};

template<typename T>
BNode<T> operator+(BNode<T> n1, BNode<T> n2) {
	BNodeInter<T> root = new BNodeInter(n1.value + n2.value, n1, n2);
	return root;
}


