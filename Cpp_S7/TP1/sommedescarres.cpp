#include <stdio.h>

int SommeDesCarres(int n)
{
	int i, somme = 0;

	for (i = 0; i <= n; i++)
		somme += i * i;

	return(somme);
}

/*
int main()
{
	int m, s;

	printf("Entrez un nombre positif : ");
	scanf("%d", &m);
	s = SommeDesCarres(m);
	printf("La somme des %d premiers entiers est %d\n", m, s);

	return 0;
}
*/