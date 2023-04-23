#include <complex.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

//Exercise 2

//Question 1
void do_nothing() {
}

//Question 2
void hello_world() {
  printf("Hello World !\n");
}

//Question 3
void sizeofstuff() {
  printf("Size of an integer is %zu byte(s)\n", sizeof(int));
  printf("Size of a char is %zu byte(s)\n", sizeof(char));
  printf("Size of a long long integer is %zu byte(s)\n", sizeof(long long int));
  printf("Size of a double is %zu byte(s)\n", sizeof(double));
  printf("Size of a float is %zu byte(s)\n", sizeof(float));
}

//Question 4
float distance_two_points(float x1, float y1, float x2, float y2) {
  return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

//Question 5
void permutation() {
  float a, b, c;
  printf("Type the value for a\n");
  scanf("%f", &a);
  printf("Type the value for b\n");
  scanf("%f", &b);
  printf("Type the value for c\n");
  scanf("%f", &c);
  printf("a : %.2f, b : %.2f, c : %.2f\n", a, b, c);
  float temp = c;
  c = b;
  b = a;
  a = temp;
  printf("a : %.2f, b : %.2f, c : %.2f\n", a, b, c);
}

//Question 6
void division() {
  int a, b, q, r;
  float qr;
  printf("Type the value for a\n");
  scanf("%d", &a);
  printf("Type the value for b\n");
  scanf("%d", &b);
  q = a / b;
  r = a % b;
  printf("Quotient of %d/%d : %d\n", a, b, q);
  printf("Remainder of %d/%d : %d\n", a, b, r);
  qr = (float)a / b;
  printf("%f\n", qr);
}

//Question 7
void solve_quadratic_equation(float a, float b, float c) {
  float delta = pow(b, 2) - 4 * a * c;
  if (delta > 0) {
    float x1, x2;
    x1 = (float)(-b - sqrt(delta)) / (2 * a);
    x2 = (float)(-b + sqrt(delta)) / (2 * a);
    printf("The solutions of %gx² + %gx + %g are x1 : %g and x2 : %g\n", a, b, c, x1, x2);
  } else {
    if (delta == 0) {
      float x;
      x = -b / (2 * a);
      printf("The solution of %gx² + %gx + %g is x : %g \n", a, b, c, x);
    } else {
      float complex z1, z2;
      z1 = (-b - sqrt(-delta) * I) / (2 * a);
      z2 = (-b + sqrt(-delta) * I) / (2 * a);
      printf("The solutions of %gx² + %gx + %g are z1 : %g + %gi and z2 : %g + %gi\n", a, b, c, crealf(z1), cimagf(z1), crealf(z2), cimagf(z2));
    }
  }
}

//Question 8
void ascii_values(char c) {
  printf("ASCII value of %c is %d in decimal, %x in hexadecimal\n", c, c, c);
}

//Question 9
//Done with the help of Loïc
void chars_to_int() {
  char a;
  int res = 0;
  bool correct = true;
  printf("Type a number\n");
  scanf("%c", &a);
  while (correct && a != 10) { //ASCII of end of line is 10
    if (isdigit(a)) {
      res = res * 10 + a - 48; //Because ASCII of 0 is 48
      scanf("%c", &a);
    } else {
      correct = false;
    }
  }
  if (correct) {
    printf("You typed %d\n", res);
  } else {
    printf("Oops, not a number\n");
    while ((getchar()) != '\n'); //Empty the buffer
    chars_to_int();
  }
}

int main() {
  chars_to_int();
  return 0;
}
