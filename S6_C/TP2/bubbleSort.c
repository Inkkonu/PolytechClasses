#include "utils.h"

void bubbleSort(int array[], int length, int(*f)(int, int)){
  for(int i = 0; i < length - 1 ; i++){
    for(int j = 0 ; j < length - i - 1 ; j++){
      if(f(array[j+1], array[j])){
        swap(&array[j], &array[j+1]);
      }
    }
  } 
}
