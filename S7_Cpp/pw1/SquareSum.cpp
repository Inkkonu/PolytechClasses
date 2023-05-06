#include <stdio.h>

int squareSum(int n)
{
	int i, sum = 0;

	for (i = 0; i <= n; i++)
		sum += i * i;

	return(sum);
}

/*
int main()
{
	int m, s;

	printf("Type a positive integer : ");
	scanf("%d", &m);
	s = squareSum(m);
	printf("The sum of the %d first integers is %d\n", m, s);

	return 0;
}
*/