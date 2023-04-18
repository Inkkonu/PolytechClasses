#pragma once
#include <iostream>

template<typename T, int R = 3, int C = 3>
class CMatrix
{
private:
	T Tab[R][C];
public:
	CMatrix() : Tab{} {};
	CMatrix(const CMatrix& m) = default;
	CMatrix(CMatrix&& m) = default;
	~CMatrix() = default;
	CMatrix& operator=(const CMatrix& m) = default;
	CMatrix& operator=(CMatrix&& m) = default;

	int& operator()(unsigned int r, unsigned int c) { return(Tab[r][c]); };
	int operator()(unsigned int r, unsigned int c) const { return(Tab[r][c]); };
	void operator+=(const double d) {
		for (unsigned int i = 0; i < R; i++) {
			for (unsigned int j = 0; j < C; j++) {
				Tab[i][j] = Tab[i][j] + d;
			}
		}
	}
	void operator-=(const double d) {
		for (unsigned int i = 0; i < R; i++) {
			for (unsigned int j = 0; j < C; j++) {
				Tab[i][j] = Tab[i][j] - d;
			}
		}
	}
	void operator*=(const double d) {
		for (unsigned int i = 0; i < R; i++) {
			for (unsigned int j = 0; j < C; j++) {
				Tab[i][j] = Tab[i][j] * d;
			}
		}
	}
	void operator/=(const double d) {
		for (unsigned int i = 0; i < R; i++) {
			for (unsigned int j = 0; j < C; j++) {
				Tab[i][j] = Tab[i][j] / d;
			}
		}
	}
};

template<typename T, int R, int C>
std::ostream& operator<<(std::ostream& os, const CMatrix<T, R, C>& m) {
	for (unsigned int i = 0; i < R; i++) {
		os << "[";
		for (unsigned int j = 0; j < C; j++) {
			os << m(i, j) << ", ";
		}
		os << "]\n";
	}
	return os;
}

