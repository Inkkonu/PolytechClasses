int compareIncreasing(int a, int b)
{
  return a <= b;
}

int compareDecreasing(int a, int b)
{
  return a >= b;
}

int compareEvenIncreasing(int a, int b)
{
  if (a % 2 == b % 2)
  {
    return a <= b;
  }
  return a % 2 == 0 && b % 2 == 1;
}

int compareOddIncreasing(int a, int b)
{
  if (a % 2 == b % 2)
  {
    return a <= b;
  }
  return a % 2 == 1 && b % 2 == 0;
}

int compareEvenDecreasing(int a, int b)
{
  if (a % 2 == b % 2)
  {
    return a >= b;
  }
  return a % 2 == 0 && b % 2 == 1;
}

int compareOddDecreasing(int a, int b)
{
  if (a % 2 == b % 2)
  {
    return a >= b;
  }
  return a % 2 == 1 && b % 2 == 0;
}
