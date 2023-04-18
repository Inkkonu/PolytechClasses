#include "B.h"
#include <iostream>

B::B() : x(0), y(0) {
	std::cout << "B()" << std::endl;
}

B::B(const B& obj) : x(obj.x), y(obj.y) {
	std::cout << "B(const B& obj)" << std::endl;
}

B::B(B&& obj) : x(obj.x), y(obj.y) {
	std::cout << "B(B&& obj)" << std::endl;
}

B::~B() {
	std::cout << "~B()" << std::endl;
}

B& B::operator=(const B& obj) {
	std::cout << "B::operator=(const B& obj)" << std::endl;

	x = obj.x;
	y = obj.y;

	return (*this);
}

B& B::operator=(B&& obj) {
	std::cout << "B::operator=(B&& obj)" << std::endl;

	x = obj.x;
	y = obj.y;

	return (*this);
}