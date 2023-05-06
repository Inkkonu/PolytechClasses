#pragma once
#include <exception>
#include <string>

class SizeException : public std::exception {
private:
	std::string ErrorMessage;

public:
	SizeException(std::string ErrMsg) : ErrorMessage(ErrMsg) {};
	std::string what() { return ErrorMessage; };
};