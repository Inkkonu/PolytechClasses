#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

// Exercise 4

// Question 1
void football_championship(int n)
{
  int receiving, moving;
  int n1 = (n % 2 == 0) ? n : n + 1; // If n is even, then n1 = n, else n1 = n+1 (Look here if you don't know ternary operator https://en.wikipedia.org/wiki/%3F:)
  for (int j = 1; j <= n1 - 1; j++)
  {
    printf("Day %d\n", j);
    for (int m = 1; m <= n1 / 2; m++)
    {
      if (m == 1)
      {
        receiving = (n % 2 == 0) ? n1 : 0;
      }
      else
      {
        receiving = ((j + m - 2) % (n1 - 1)) + 1;
      }
      moving = ((j - m + n1 - 1) % (n1 - 1)) + 1;
      if (moving != 0 && receiving != 0)
      {
        printf("%d-%d\n", receiving, moving);
      }
    }
  }
}

// Question 2
void calculator()
{
  char c;
  bool correct = true;
  int a = 0, b = 0, res;
  char operator;
  printf("Type your operation\n");
  scanf("%c", &c);
  while (isdigit(c))
  {
    a = a * 10 + c - 48; // Because ASCII of 0 is 48
    scanf("%c", &c);
  }
  operator= c;
  c = getchar();
  while (isdigit(c))
  {
    b = b * 10 + c - 48; // Because ASCII of 0 is 48
    scanf("%c", &c);
  }
  if (c != '=')
  {
    correct = false;
  }
  switch (operator)
  {
  case '+':
    res = a + b;
    break;
  case '-':
    res = a - b;
    break;
  case '*':
    res = a * b;
    break;
  case '/':
    if (b == 0)
    {
      printf("You can't divide by 0 you idiot!!\n");
      correct = false;
    }
    else
    {
      res = a / b;
    }
    break;
  case '%':
    res = a % b;
    break;
  default:
    correct = false;
  }
  if (correct)
  {
    printf("%d%c%d=%d\n", a, operator, b, res);
  }
  else
  {
    printf("Oops, your operation doesn't seem to be correct\n");
  }
}

int main()
{
  calculator();
  return 0;
}
