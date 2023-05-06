#include "A.h"
#include <iostream>

A::A() : x(0), y(0) {
	std::cout << "A()" << std::endl;
}

A::A(const A& obj) : x(obj.x), y(obj.y) {
	std::cout << "A(const A& obj)" << std::endl;
}

A::A(A&& obj) : x(obj.x), y(obj.y) {
	std::cout << "A(A&& obj)" << std::endl;
}

A::~A() {
	std::cout << "~A()" << std::endl;
}

A& A::operator=(const A& obj) {
	std::cout << "A::operator=(const A& obj)" << std::endl;

	x = obj.x;
	y = obj.y;

	return (*this);
}

A& A::operator=(A&& obj) {
	std::cout << "A::operator=(A&& obj)" << std::endl;

	x = obj.x;
	y = obj.y;

	return (*this);
}

A::A(const B& b) : x(b.GetX()), y(b.GetY()) {
	std::cout << "A(const B& b)" << std::endl;
}