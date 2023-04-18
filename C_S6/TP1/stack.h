#ifndef STACK_H_
#define STACK_H_

struct _Stack {
  char array[100][100];
  int index;
};

typedef struct _Stack Stack;

void stackInit(Stack *stack);

int stackSize(Stack *stack);

char *stackTop(Stack *stack);

void stackPush(Stack *stack, char *element);

void stackPop(Stack *stack);

#endif
