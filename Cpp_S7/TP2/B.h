#pragma once

class B {
private:
	double x;
	double y;

public:
	B();
	B(const B& obj);
	B(B&& obj);
	~B();
	B& operator=(const B& obj);
	B& operator=(B&&);

	inline double GetX() const { return x; };
	inline double GetY() const { return y; };
};