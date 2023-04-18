#include "Vector.h"
#include "OutOfRangeException.h"
#include "NullException.h"
#include "SizeException.h"
#include "DivisionByZeroException.h"

Vector::Vector() : Vec(nullptr), Size(0){}

Vector::Vector(const Vector& v)
{
	Size = v.Size;
	Vec = (double*)malloc(Size * sizeof(double));
	if (Vec == nullptr || v.Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
	for (unsigned int i = 0; i < v.Size; i++) Vec[i] = v.Vec[i];
}

Vector::Vector(Vector&& v) : Vec(v.Vec), Size(v.Size)
{
	v.Vec = nullptr;
	v.Size = 0;
}

Vector::Vector(const double* tab, unsigned int size)
{
	Size = size;
	Vec = (double*)malloc(size * sizeof(double));
	if (Vec == nullptr || tab == nullptr) {
		throw NullException("Null pointer exception");
	}
	for (unsigned int i = 0; i < size; ++i) Vec[i] = tab[i];
}

Vector::~Vector()
{
	free(Vec);
}

Vector& Vector::operator=(const Vector& v)
{
	Size = v.Size;
	free(Vec);
	Vec = (double*)malloc(Size * sizeof(double));
	if (Vec == nullptr || v.Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
	for (unsigned int i = 0; i < v.Size; ++i) Vec[i] = v.Vec[i];

	return(*this);
}

Vector& Vector::operator=(Vector&& v)
{
	Vec = v.Vec;
	Size = v.Size;
	v.Vec = nullptr;
	v.Size = 0;

	return(*this);
}

void Vector::AddData(double d)
{
	Size++;
	Vec = (double*)realloc(Vec, Size * sizeof(double));
	if (Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
	Vec[Size - 1] = d;
}

void Vector::AddVector(const double* v, unsigned int size)
{
	Vec = (double*)realloc(Vec, (Size + size) * sizeof(double));
	if (Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
	for (unsigned int i = 0; i < size; ++i) Vec[Size + i] = v[i];
	Size += size;
}

void Vector::ReplaceVector(const double* v, unsigned int size)
{
	Size = size;
	free(Vec);
	Vec = (double*)malloc(Size * sizeof(double));
	if (Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
	for (unsigned int i = 0; i < size; ++i) Vec[i] = v[i];
}

void Vector::Reserve(unsigned int size)
{
	Size = size;
	Vec = (double*)realloc(Vec, Size * sizeof(double));
	if (Vec == nullptr) {
		throw NullException("Null pointer exception");
	}
}

double& Vector::operator[](unsigned int i) {
	if (i < 0 || i >= Size) {
		throw OutOfRangeException("Index out of range");
	}
	return(Vec[i]);
}

double Vector::operator[](unsigned int i) const {
	if (i < 0 || i >= Size) {
		throw OutOfRangeException("Index out of range");
	}
	return(Vec[i]);
}

void Vector::Homothecy(double h)
{
	for (unsigned int i = 0; i < Size; ++i) Vec[i] *= h;
}

double Vector::Norm()
{
	double norm = 0;

	for (unsigned int i = 0; i < Size; ++i) norm += Vec[i] * Vec[i];
	norm = std::sqrt(norm);

	return norm;
}

double Vector::EuclideanDistance(const Vector& v1, const Vector& v2)
{
	if (v1.Size != v2.Size)
	{
		throw SizeException("The vectors are not of the same size");
	}

	double dist = 0;

	for (unsigned int i = 0; i < v1.Size; ++i) dist += (v2.Vec[i] - v1.Vec[i]) * (v2.Vec[i] - v1.Vec[i]);
	dist = std::sqrt(dist);

	return dist;
}

Vector operator+(const Vector& v1, const Vector& v2) {
	if (v1.GetSize() != v2.GetSize()) {
		throw SizeException("The vectors are not of the same size");
	}
	Vector v;
	for (unsigned int i = 0; i < v1.GetSize(); i++) {
		v.AddData(v1[i] + v2[i]);
	}
	return v;
}

Vector operator-(const Vector& v1, const Vector& v2) {
	if (v1.GetSize() != v2.GetSize()) {
		throw SizeException("The vectors are not of the same size");
	}
	Vector v;
	for (unsigned int i = 0; i < v1.GetSize(); i++) {
		v.AddData(v1[i] - v2[i]);
	}
	return v;
}

Vector operator-(const Vector& v1) {
	Vector v;
	for (unsigned int i = 0; i < v1.GetSize(); i++) v.AddData(-v1[i]);
	return v;
}

Vector operator/(const Vector& v1, double d) {
	if (d == 0) {
		throw DivisionByZeroException("Stop trying to divide by zero!");
	}
	Vector v;
	for (unsigned int i = 0; i < v1.GetSize(); i++) v.AddData(v1[i] / d);
	return v;
}

Vector operator*(const Vector& v1, const Vector& v2) {
	if (v1.GetSize() != v2.GetSize()) {
		throw SizeException("The vectors are not of the same size");
	}
	Vector v;
	for (unsigned int i = 0; i < v1.GetSize(); i++) {
		v.AddData(v1[i] * v2[i]);
	}
	return v;
}

void operator*=(Vector& v1, double d) {
	for (unsigned int i = 0; i < v1.GetSize(); i++) v1[i] = v1[i] * d;
}

bool operator==(const Vector& v1, const Vector& v2) {
	if (v1.GetSize() != v2.GetSize()) {
		return false;
	}
	else {
		unsigned int i = 0;
		while (i < v1.GetSize() && v1[i] == v2[i]) {
			i++;
		}
		return i == v1.GetSize();
	}
}

bool operator!=(const Vector& v1, const Vector& v2) {
	return !(v1 == v2);
}


std::ostream& operator<<(std::ostream& os, const Vector& v)
{
	os << "[";
	for (unsigned int i = 0; i < v.GetSize(); i++) {
		os << v[i];
		if (i != v.GetSize() - 1) {
			os << ", ";
		}
	}
	os << "]";
	return os;
}

std::istream& operator>>(std::istream& is, Vector& v) {
	double d;
	is >> d;
	v.AddData(d);

	return is;
}
