#include <stdlib.h>
#include <stdio.h>
#include "List.h"

void PrintList(SList *list);

int main()
{
	SList *list;
	SCell *cell;

	list = CreateList();

	printf("Add 5, 3, 1\n");
	AddElementBegin(list, 5);
	cell = AddElementBegin(list, 3);
	AddElementBegin(list, 1);
	PrintList(list);
	printf("\n");

	printf("Add 6, 7\n");
	AddElementEnd(list, 6);
	AddElementEnd(list, 7);
	PrintList(list);
	printf("\n");

	printf("Add 4\n");
	AddElementAfter(list, cell, 4);
	PrintList(list);
	printf("\n");

	printf("Add 2\n");
	AddElementAfter(list, GetFirstElement(list), 2);
	PrintList(list);
	printf("\n");

	printf("Delete 3\n");
	DeleteCell(list, cell);
	PrintList(list);
	printf("\n");

	DeleteList(list);

	return 0;
}

void PrintList(SList *list)
{
	if (list)
	{
		SCell *cell = GetFirstElement(list);
		while (cell != NULL)
		{
			printf("[%d] -> ", GetData(cell));
			cell = GetNextElement(cell);
		}
		printf("NULL\n");
	}
}
