#pragma once
#include <exception>
#include <string>

class NullException : public std::exception {
private:
	std::string ErrorMessage;

public:
	NullException(std::string ErrMsg) : ErrorMessage(ErrMsg) {};
	std::string what() { return ErrorMessage; };
};