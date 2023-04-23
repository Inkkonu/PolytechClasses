#include "CPile.h"
#include "FullStackException.h"
#include "NoElementException.h"

CPile& CPile::operator<(const int& v) {
	if (GetSize() != MaxSize) {
		LastIndex++;
		Tab[LastIndex] = v;
	}
	else {
		throw FullStackException();
	}
	return (*this);
}

CPile& CPile::operator>(int& v) {
	if (GetSize() > 0) {
		v = Tab[LastIndex];
		LastIndex--;
	}
	else {
		throw NoElementException();
	}
	return (*this);
}