#pragma once
#include <algorithm>

template <class T> void SwapT(T& a, T& b) {
	T tmp = std::move(a);
	a = std::move(b);
	b = std::move(tmp);
}
