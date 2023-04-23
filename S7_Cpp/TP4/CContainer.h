#pragma once
#include "CStack.h"

class CContainer
{
public:
	explicit CContainer(unsigned int MaximumSize = 10);
	CStack*& operator[](unsigned int i);
	CStack* operator[](unsigned int i) const;
private:
	CStack** Tab;
	unsigned int MaxSize;
};

