#include "utils.h"

int partition(int array[], int low, int high, int(*f)(int, int)) {
  int pivot = array[high];
  int i = (low - 1);

  for (int j = low; j < high; j++) {
    if(f(array[j], pivot)){
      i++;
      swap(&array[i], &array[j]);
    }
  }
  swap(&array[i + 1], &array[high]);
  return (i + 1);
}


void _quickSort(int array[], int low, int high, int(*f)(int, int)) {
  if (low < high) {
    int p = partition(array, low, high, f);
    _quickSort(array, low, p - 1, f);
    _quickSort(array, p + 1, high, f);
  }
}

void quickSort(int array[], int length, int(*f)(int, int)) {
  _quickSort(array, 0, length-1, f);
}
