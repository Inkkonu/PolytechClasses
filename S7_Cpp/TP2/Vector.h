#pragma once

class Vector {
private:
	unsigned int Size;
	double* Vec;

public:
	Vector() : Size(0), Vec(nullptr) {};
	Vector(double* tab, unsigned int size);
	Vector(const Vector& v);
	Vector(Vector&& v);
	~Vector();
	Vector& operator=(const Vector& v);
	Vector& operator=(Vector&& v);

	inline double& operator[](unsigned int i) { return(Vec[i]); };
	inline double operator[](unsigned int i) const { return(Vec[i]); };

	inline unsigned int GetSize() const { return Size; }; //In .h because it's just a return
	inline const double* GetVector() const { return Vec; };

	void AddData(double d);
	void AddVector(const double* v, unsigned int size);
	void ReplaceVector(const double* v, unsigned int size);
	void Reserve(unsigned int size);
	void Homothecy(double d);
	double Norm();
	double EuclideanDistance(const Vector &v1, const Vector& v2);
};