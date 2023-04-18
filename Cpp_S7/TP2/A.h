#pragma once
#include "B.h"

class A {
private:
	double x;
	double y;

public:
	A();
	A(const A& obj);
	A(A&& obj);
	~A();
	A& operator=(const A& obj);
	A& operator=(A&&);

	A(const B& b);

	inline double GetX() const { return x; };
	inline double GetY() const { return y; };
};