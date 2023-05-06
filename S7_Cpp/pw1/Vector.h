#pragma once

class Vector {
private:
	unsigned int Size;
	double* Vec;

public:
	Vector() : Size(0), Vec(nullptr) {};
	Vector(double* vec, unsigned int size) : Size(size), Vec(vec) {};
	Vector(const Vector& v);
	Vector(Vector&& v);
	~Vector();
	Vector& operator=(const Vector& v);
	Vector& operator=(Vector&& v);

	inline unsigned int GetSize() const { return Size; }; //In .h because it's just a return
	inline const double* GetVector() const { return Vec; };
	void AddData(double d);
	void AddVector(const double* v, unsigned int size);
	void ReplaceVector(const double* v, unsigned int size);
};