#include "Vector.h"
#include <cstdlib>
#include <cmath>
#include <iostream>

Vector::Vector(double* tab, unsigned int size) {
	Size = size;
	Vec = (double*)malloc(size * sizeof(double));
	for (unsigned int i = 0; i < Size; i++) Vec[i] = tab[i];
}

Vector::Vector(const Vector& v) : Size(v.Size) {
	free(Vec);
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

void Vector::Reserve(unsigned int size) {
	Size = size;
	Vec = (double*)realloc(Vec, Size * sizeof(double));
}

void Vector::Homothecy(double d) {
	for (unsigned int i = 0; i < Size; i++) Vec[i] *= d;
}

double Vector::Norm() {
	double norm = 0;

	for (unsigned int i = 0; i < Size; i++) norm += Vec[i] * Vec[i];
	norm = std::sqrt(norm);

	return norm;
}

double Vector::EuclideanDistance(const Vector& v1, const Vector& v2) {
	if (v1.Size != v2.Size) {
		printf("v1 and v2 not the same size");
	}

	double dist = 0;
	for (unsigned int i = 0; i < v1.Size; i++) dist += (v2.Vec[i] - v1.Vec[i]) * (v2.Vec[i] - v1.Vec[i]);
	dist = std::sqrt(dist);

	return dist;
}