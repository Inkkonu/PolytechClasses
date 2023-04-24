#ifndef COMPAREFUNCTIONS_H_
#define COMPAREFUNCTIONS_H_

#include <stdio.h>

int compareIncreasing(int a, int b);

int compareDecreasing(int a, int b);

/**
 * Puts the even numbers first, then the odd but they are sorted in an increasing order among them
 */
int compareEvenIncreasing(int a, int b);

/**
 * Puts the odd numbers first, then the even but they are sorted in an increasing order among them
 */
int compareOddIncreasing(int a, int b);

/**
 * Puts the even numbers first, then the odd but they are sorted in an decreasing order among them
 */
int compareEvenDecreasing(int a, int b);

/**
 * Puts the odd numbers first, then the even but they are sorted in an decreasing order among them
 */
int compareOddDecreasing(int a, int b);

#endif
