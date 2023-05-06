#pragma once
#include <iostream>

//I used size_t because apparently it's better (COPIUM) but I have no idea why
template<typename T, size_t R = 3, size_t C = 3>
class CMatrix
{
public:
	CMatrix() : Tab{} {};
	CMatrix(const CMatrix& m) = default;
	CMatrix(CMatrix&& m) = default;
	~CMatrix() = default;
	CMatrix& operator=(const CMatrix& m) = default;
	CMatrix& operator=(CMatrix&& m) = default;

	CMatrix(const std::initializer_list<T>& args);

	T& operator()(size_t r, size_t c) { return(Tab[r][c]); };
	T operator()(size_t r, size_t c) const { return(Tab[r][c]); };
	CMatrix& operator+=(const T& value) { return(Op([](T& data, const T& value) { data += value; }, value)); };
	CMatrix& operator-=(const T& value) { return(Op([](T& data, const T& value) { data -= value; }, value)); };
	CMatrix& operator*=(const T& value) { return(Op([](T& data, const T& value) { data *= value; }, value)); };
	CMatrix& operator/=(const T& value) { return(Op([](T& data, const T& value) { data /= value; }, value)); };

private:
	T Tab[R][C];

	template<typename F>
	CMatrix& Op(F&& pf, const T& value);
};

template<typename T, size_t R, size_t C>
CMatrix<T, R, C>::CMatrix(const std::initializer_list<T>& args) {
	if (args.size() != R * C) {
		throw std::invalid_argument("Parameter is not of the correct size");
	}
	size_t i = 0, j = 0;
	for (const T& arg : args) {
		Tab[i][j] = arg;
		j++;
		if (j == C) {
			j = 0;
			i++;
		}
	}
}

template<typename T, size_t R, size_t C>
template<typename F>
CMatrix<T, R, C>& CMatrix<T, R, C>::Op(F&& pf, const T& value) {
	for (size_t i = 0; i < R; i++) {
		for (size_t j = 0; j < C; j++) {
			pf(Tab[i][j], value);
		}
	}
	return (*this);
}

template<typename T1, typename T2, size_t N>
auto Dot(const CMatrix<T1, 1, N>& m1, const CMatrix<T2, 1, N>& m2) -> decltype((m1(0, 0) + m2(0, 0))* (m1(0, 0) + m2(0, 0))) {
	decltype((m1(0, 0) + m2(0, 0)) * (m1(0, 0) + m2(0, 0))) result = {};
	for (size_t i = 0; i < N; i++) {
		result += m1(0, i) * m2(0, i);
	}
	return(result);
}

template<typename T1, typename T2, size_t r1, size_t c1, size_t c2>
auto operator*(const CMatrix<T1, r1, c1>& m1, const CMatrix<T2, c1, c2>& m2) -> CMatrix<decltype((m1(0, 0) + m2(0, 0))* (m1(0, 0) + m2(0, 0))), r1, c2> {
	CMatrix<decltype((m1(0, 0) + m2(0, 0))* (m1(0, 0) + m2(0, 0))), r1, c2> m3 = {};
	for (size_t i = 0; i < r1; i++) {
		for (size_t j = 0; j < c2; j++) {
			for (size_t k = 0; k < c1; k++) {
				m3(i, j) += m1(i, k) * m2(k, j);
			}
		}
	}
	return m3;
}

template<typename T, size_t R, size_t C>
std::ostream& operator<<(std::ostream& os, const CMatrix<T, R, C>& m) {
	for (size_t i = 0; i < R; i++) {
		os << "[";
		for (size_t j = 0; j < C; j++) {
			os << m(i, j) << ", ";
		}
		os << "]\n";
	}
	return os;
}

