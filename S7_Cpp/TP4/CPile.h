#pragma once
#include "CStack.h"
#include <iostream>

class CPile : public CStack 
{
private:
	unsigned int LastIndex;
public:
	explicit CPile(unsigned int MaxSize = 10) : CStack(MaxSize), LastIndex(-1) {};
	CPile(const CPile& s) = default;
	CPile(CPile&& s) = default;
	virtual ~CPile() {};
	CPile& operator=(const CPile& s) = default;
	CPile& operator=(CPile&& s) = default;

	inline unsigned int GetSize() { return LastIndex + 1; };
	CPile& operator<(const int& v);
	CPile& operator>(int& v);
};