#pragma once
#include "CStack.h"

class CFile : public CStack
{
private:
	unsigned int FirstIndex;
	unsigned int LastIndex;
public:
	explicit CFile(unsigned int MaxSize = 10) : CStack(MaxSize), FirstIndex(-1), LastIndex(-1) {};
	CFile(const CFile& s) = default;
	CFile(CFile&& s) = default;
	virtual ~CFile() {};
	CFile& operator=(const CFile& s) = default;
	CFile& operator=(CFile&& s) = default;

	unsigned int GetSize();
	CFile& operator<(const int& v);
	CFile& operator>(int& v);
};

