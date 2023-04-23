#pragma once
#include <iostream>

class FullStackException : public std::exception {
private:
	const char* message;
public:
	FullStackException() : message("The stack is full, can't stack") {};
	const char* what() {
		return message;
	}
};