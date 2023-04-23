#include "Vector.h"

int main() {
	double tab[] = { 1.0,2.0,3.0 };
	Vector v(tab, 3);
	v[0] = 10;

	const Vector& cv = v;
	double val = cv[2];

	return 0;
}