#pragma once
#include <iostream>
#include <cmath>
#include <cstdlib>

class Vector
{
public:
	Vector();
	Vector(const Vector& v);
	Vector(Vector&& v);
	Vector(const double* tab, unsigned int size);
	~Vector();
	Vector& operator=(const Vector& v);
	Vector& operator=(Vector&& v);
	inline const double* GetVector() const { return(Vec); }
	inline unsigned int GetSize() const { return(Size); }
	void AddData(double d);
	void AddVector(const double* v, unsigned int size);
	void ReplaceVector(const double* v, unsigned int size);
	void Reserve(unsigned int size);
	double& operator[](unsigned int i);
	double operator[](unsigned int i) const;
	void Homothecy(double h);
	double Norm();
	static double EuclideanDistance(const Vector& v1, const Vector& v2);
	
private:
	double* Vec;
	unsigned int Size;
};

Vector operator+(const Vector& v1, const Vector& v2);
Vector operator-(const Vector& v1, const Vector& v2);
Vector operator-(const Vector& v1);
Vector operator/(const Vector& v1, double d);
Vector operator*(const Vector& v1, const Vector& v2);
void operator*=(Vector& v1, double d);
bool operator==(const Vector& v1, const Vector& v2);
bool operator!=(const Vector& v1, const Vector& v2);

std::ostream& operator<<(std::ostream& os, const Vector& v);
std::istream& operator>>(std::istream& in, Vector& v);