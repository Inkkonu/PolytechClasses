#include "Vector.h"
#include <cstdlib>

Vector::Vector(const Vector& v) : Size(v.Size) {
	Vec = (double*)malloc(Size * sizeof(double));
	for (unsigned int i = 0; i < Size; i++) Vec[i] = v.Vec[i];
}

Vector::Vector(Vector&& v) : Size(v.Size), Vec(v.Vec) {
	v.Size = 0;
	v.Vec = nullptr;
}

Vector::~Vector() {
	free(Vec);
}

Vector& Vector::operator=(const Vector& v) {
	Size = v.Size;
	free(Vec);
	Vec = (double*)malloc(Size * sizeof(double));
	for (unsigned int i = 0; i < Size; i++) Vec[i] = v.Vec[i];

	return (*this);
}

Vector& Vector::operator=(Vector&& v) {
	Vec = v.Vec;
	Size = v.Size;
	v.Vec = nullptr;
	v.Size = 0;

	return (*this);
}

void Vector::AddData(double d) {
	Size++;
	Vec = (double*)realloc(Vec, Size * sizeof(double));
	Vec[Size - 1] = d;
}

void Vector::AddVector(const double* v, unsigned int size) {
	Vec = (double*)realloc(Vec, (Size + size) * sizeof(double));
	for (unsigned int i = 0; i < size; i++) Vec[Size + i] = v[i];
	Size += size;
}

void Vector::ReplaceVector(const double* v, unsigned int size) {
	Size = size;
	free(Vec);
	Vec = (double*)malloc(size * sizeof(double));
	for (unsigned int i = 0; i < size; i++) Vec[i] = v[i];
}