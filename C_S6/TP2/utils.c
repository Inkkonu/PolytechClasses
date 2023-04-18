#include <stdbool.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int *random_array(int n) {
  int *array = malloc(sizeof(int) * n);
  srand(time(NULL)); //Seed the random generator to time to make it random
  for (int i = 0; i < n; i++) {
    array[i] = rand();
  }
  return array;
}

bool is_sorted(int array[], int n) {
  int i = 1;
  while (i < n && array[i] >= array[i - 1]) {
    i++;
  }
  int j = 1;
  while (j < n && array[j] <= array[j - 1]) {
    j++;
  }
  return i == n || j == n;
}
