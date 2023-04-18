#include <iostream>
#include "main.h"
#include "CMatrix.h"

int main() {
	int i = 5; int j = 6;
	std::cout << "i=" << i << " ; j=" << j << std::endl;
	SwapT<int>(i, j);
	std::cout << "i=" << i << " ; j=" << j << std::endl;

	double f = 5.55, g = 6.66;
	std::cout << "f=" << f << " ; g=" << g << std::endl;
	SwapT<double>(f, g);
	std::cout << "f=" << f << " ; g=" << g << std::endl;

	std::string s = "chaine 1", t = "chaine 2";
	std::cout << "s=" << s << " ; t=" << t << std::endl;
	SwapT(s, t);
	std::cout << "s=" << s << " ; t=" << t << std::endl;

	CMatrix<int,2,2> m;
	m(0, 1) = 4;
	m(1, 1) = 1;
	std::cout << m;

	return 0;
}