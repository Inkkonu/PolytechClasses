#pragma once
#include <exception>
#include <string>

class OutOfRangeException : public std::exception {
private:
	std::string ErrorMessage;

public:
	OutOfRangeException(std::string ErrMsg) : ErrorMessage(ErrMsg){};
	std::string what() { return ErrorMessage; };
};