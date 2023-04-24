#ifndef QUICKSORT_H_
#define QUICKSORT_H_

#include <stdio.h>
#include "utils.h"

int partition(int array[], int low, int high, int (*f)(int, int));

/**
 * The function called by quickSort()
 */
void _quickSort(int array[], int low, int high, int (*f)(int, int));

/**
 * The function called by the user
 */
void quickSort(int array[], int length, int (*f)(int, int));

#endif
