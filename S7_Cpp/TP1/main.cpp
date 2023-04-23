#include "Vector.h"
#include <stdio.h>

#define DebugVector(v) {printf(#v"=");PrintVector(v);}

void PrintVector(const Vector& v)
{
	printf("[");
	for (unsigned int i = 0; i < v.GetSize(); ++i)
	{
		if (i != 0) printf(", ");
		printf("%f", v.GetVector()[i]);
	}
	printf("]\n");
}

int main()
{
	double tab1[5] = { 1.0, 2.0, 3.0, 4.0, 5.0 };
	double tab2[3] = { 6.0, 7.0, 8.0 };
	double tab3[2] = { 9.0, 10.0 };
	Vector v1(tab1, 5);
	Vector v2;

	v2.AddVector(tab2, 3);
	DebugVector(v1);
	DebugVector(v2);
	/*
	Renvoi sur le terminal :
	v1=[1.0, 2.0, 3.0, 4.0, 5.0]
	v2=[6.0, 7.0, 8.0]
	*/

	Vector v3(v1);
	v1.AddData(11);
	v2.ReplaceVector(tab3, 2);
	DebugVector(v1);
	DebugVector(v2);
	DebugVector(v3);
	/*
	Renvoi sur le terminal :
	v1=[1.0, 2.0, 3.0, 4.0, 5.0, 11.0]
	v2=[9.0, 10.0]
	v3=[1.0, 2.0, 3.0, 4.0, 5.0]
	*/

	return 0;
}