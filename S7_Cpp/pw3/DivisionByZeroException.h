#pragma once
#include <exception>
#include <string>

class DivisionByZeroException : public std::exception {
private:
	std::string ErrorMessage;

public:
	DivisionByZeroException(std::string ErrMsg) : ErrorMessage(ErrMsg) {};
	std::string what() { return ErrorMessage; };
};