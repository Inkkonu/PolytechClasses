#include "CContainer.h"
#include <iostream>

CContainer::CContainer(unsigned int MaximumSize) : MaxSize(MaximumSize) {
	Tab = new CStack * [MaximumSize];
}

CStack*& CContainer::operator[](unsigned int i) {
	if (i < 0 || i >= MaxSize) {
		throw std::invalid_argument("Index out of range");
	}
	return(Tab[i]);
}

CStack* CContainer::operator[](unsigned int i) const {
	if (i < 0 || i >= MaxSize) {
		throw std::invalid_argument("Index out of range");
	}
	return(Tab[i]);
}
