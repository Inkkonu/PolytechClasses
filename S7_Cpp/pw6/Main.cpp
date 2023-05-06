#include "CMatrix.h"

int main() {
	CMatrix<int, 2, 2> m1 = { 1,4,1,1 };
	CMatrix<int, 2, 2> m2 = { 2,3,2,3 };

	auto r = m1 * m2;

	std::cout << r;

	return 0;
}