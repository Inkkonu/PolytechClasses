#include "stack.h"
#include <stdio.h>
#include <string.h>

void stackInit(Stack *stack)
{
  stack->index = 0;
}

int stackSize(Stack *stack)
{
  return stack->index;
}

char *stackTop(Stack *stack)
{
  return stack->array[stack->index - 1];
}

void stackPush(Stack *stack, char *element)
{
  strcpy(stack->array[stack->index], element);
  stack->index++;
}

void stackPop(Stack *stack)
{
  stack->index--;
}