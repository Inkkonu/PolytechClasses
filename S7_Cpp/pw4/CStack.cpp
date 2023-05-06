#include "CStack.h"
#include <iostream>

CStack::CStack(unsigned int MaximumSize) : MaxSize(MaximumSize) {
	Tab = new int[MaxSize];
}

CStack::CStack(const CStack& s) : MaxSize(s.MaxSize) {
	Tab = new int[MaxSize];
	std::copy(s.Tab, s.Tab + s.MaxSize, Tab);
}

CStack::CStack(CStack&& s) {
	Tab = s.Tab;
	delete[] s.Tab;
	MaxSize = std::move(s.MaxSize);
}

CStack::~CStack() {
	delete[] Tab;
}

CStack& CStack::operator=(const CStack& s) {
	MaxSize = s.MaxSize;
	delete[] Tab;
	Tab = new int[MaxSize];
	std::copy(s.Tab, s.Tab + s.MaxSize, Tab);

	return (*this);
}

CStack& CStack::operator=(CStack&& s) {
	MaxSize = std::move(s.MaxSize);
	delete[] Tab;
	Tab = s.Tab;
	delete[] s.Tab;

	return (*this);
}