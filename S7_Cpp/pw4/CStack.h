#pragma once

class CStack
{
protected:
	int* Tab;
	unsigned int MaxSize;
public:
	explicit CStack(unsigned int MaximumSize = 10);
	CStack(const CStack& s);
	CStack(CStack&& s);
	virtual ~CStack();
	CStack& operator=(const CStack& s);
	CStack& operator=(CStack&& s);
	unsigned int GetMaxSize() const { return MaxSize; };

	virtual unsigned int GetSize() = 0;
	virtual CStack& operator<(const int& v) = 0;
	virtual CStack& operator>(int& v) = 0;
};
