#pragma once
#include <iostream>

class NoElementException : public std::exception {
private:
	const char* message;
public:
	NoElementException() : message("No element in the stack, can't unstack") {};
	const char* what() {
		return message;
	}
};