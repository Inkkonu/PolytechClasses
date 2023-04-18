#ifndef UTILS_H_
#define UTILS_H_

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void swap(int *a, int *b);

int *random_array(int n);

/**
 * Only returns true if the array is linear
 * If the array is sorted even numbers first, then the odd, it will return false
 */
bool is_sorted(int array[], int n);

#endif
