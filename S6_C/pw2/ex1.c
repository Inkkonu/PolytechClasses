#include <stdio.h>
#include <time.h>
#include "bubbleSort.h"
#include "quickSort.h"
#include "compareFunctions.h"
#include "utils.h"

#define ARRAYLENGTH 50000

#define ALGO(name) {#name, name},
#define ALGOTERM() {NULL, NULL},

struct SAlgo
{
  char *Name;
  void (*Function)(int[], int, int (*fnCmp)(int, int));
};

struct SAlgo Algos[] = {
    ALGO(bubbleSort)
        ALGO(quickSort)
            ALGOTERM()};

void sortingTest(int length)
{
  clock_t start_t, end_t, total_t;
  for (int i = 0; i < length; i++)
  {
    int *array = random_array(ARRAYLENGTH);
    start_t = clock();
    Algos[i].Function(array, ARRAYLENGTH, compareIncreasing);
    end_t = clock();
    printf("Time taken by %s : %fs\n", Algos[i].Name, (double)(end_t - start_t) / CLOCKS_PER_SEC);
    fflush(stdout);
  }
}

int main()
{
  sortingTest(2);
  return 0;
}
