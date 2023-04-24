#include <stdio.h>
#include <string.h>

// Exercise 3

// Question 1
void print_matrix(int rows, int cols, int matrix[rows][cols])
{
  for (int i = 0; i < rows; i++)
  {
    printf("| ");
    for (int j = 0; j < cols; j++)
    {
      printf("%d\t", matrix[i][j]);
    }
    printf("|\n");
  }
}

// Question 2
void ask_for_matrix()
{
  int matrix[3][3];
  for (int i = 0; i < 9; i++)
  {
    printf("Type a number for the matrix\n");
    scanf("%d", &matrix[i / 3][i % 3]);
  }
  print_matrix(3, 3, matrix);
}

int main()
{
  ask_for_matrix();
  return 0;
}
