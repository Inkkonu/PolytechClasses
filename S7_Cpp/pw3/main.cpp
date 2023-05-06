#include "Vector.h"
#include <iostream>
#include "OutOfRangeException.h"
#include "DivisionByZeroException.h"
#include "NullException.h"
#include "SizeException.h"

int main() {
	double tab1[3] = { 1.0,3.0,5.0 };
	double tab2[3] = { 0.0,4.0,6.0 };
	double tab3[4] = { 1.0,3.0,5.0,12.7 };

	Vector v1(tab1, 3);
	Vector v2(tab2, 3);
	Vector v3(tab3, 4);
	Vector v4;

	std::cout << "v1=" << v1 << std::endl;
	std::cout << "v2=" << v2 << std::endl;
	std::cout << "v3=" << v3 << std::endl;
	std::cout << "\n";

	try {
		std::cout << "Testing +" << std::endl;

		std::cout << "v1 + v2 = ";
		v4 = v1 + v2;
		std::cout << v4 << std::endl;

		std::cout << "v1 + v3 = ";
		v4 = v1 + v3;
		std::cout << v4 << std::endl;
	}
	catch (SizeException e) {
		std::cout << e.what() << std::endl;
	}

	std::cout << "\n";

	try {
		std::cout << "Testing []" << std::endl;

		std::cout << "v1[0] = ";
		std::cout << v1[0] << std::endl;

		std::cout << "v1[15] = ";
		std::cout << v1[15] << std::endl;
	}
	catch (OutOfRangeException e) {
		std::cout << e.what() << std::endl;
	}

	std::cout << "\n";

	try {
		std::cout << "Testing /" << std::endl;

		std::cout << "v1 / 2.0 = ";
		v4 = v1 / 2.0;
		std::cout << v4 << std::endl;

		std::cout << "v1 / 0.0 = ";
		v4 = v1 / 0.0;
		std::cout << v4 << std::endl;
	}
	catch (DivisionByZeroException e) {
		std::cout << e.what() << std::endl;
	}

	return 0;
}