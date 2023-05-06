#pragma once
#include <iostream>

template<int i, typename T>
class Array
{
public:
	Array() : tab{} {};
	~Array() = default;
	int size() const { return i; };
	T& operator[](unsigned int idx) { return(tab[idx]); };
	T operator[](unsigned int idx) const { return(tab[idx]); };
protected:
	T tab[i];
};

template<int i, typename T, typename F>
void Aggregate(Array<i, T>& arr, const F&& func) {
	for (int j = 0; j < arr.size(); j++) {
		func(arr[j]);
	}
}

