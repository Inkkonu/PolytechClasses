#pragma once
#include <vector>
#include "BNode.h"
#include "BNodeLeaf.h"

template<typename T>
class Forest
{
public:
	Forest();
	Forest(const Forest&); // Constructeur de recopie
	Forest(Forest&&); // Constructeur de déplacement
	Forest(const std::initializer_list<T>& args);
	~Forest(); // Destructeur éventuellement virtuel
	Forest& operator=(const Forest&); // Opérateur d’affectation
	Forest& operator=(Forest&&); // Opérateur de déplacement

	void AddValue(T v, unsigned char c);

	void Glouton();
private:
	// A vector is a good solution because it is resizable
	std::vector<BNode<T>> trees;
};

template<typename T>
Forest<T>::Forest(const std::initializer_list<T>& args)
{
	for (const T& arg : args) {
		AddValue(arg);
	}
}

template<typename T>
Forest<T>::~Forest() {
	for (BNode<T> node : trees) {
		node.~BNode();
	}
}

template<typename T>
void Forest<T>::AddValue(T v, unsigned char c)
{
	BNodeLeaf<T> leaf = BNodeLeaf(v, c);
	trees.push_back(leaf);
}

template<typename T>
void Forest<T>::Glouton() {
	while (trees.size() > 1) {
		std::sort(trees.begin(), trees.end(), [](BNode<T> n1, BNode<T> n2) {
			return n1.GetValue() < n2.GetValue();
			});
		BNode<T1> n1 = trees[0];
		BNode<T1> n2 = trees[1];
		trees.erase(0);
		trees.erase(1);
		trees.push_back(n1 + n2);
	}
}