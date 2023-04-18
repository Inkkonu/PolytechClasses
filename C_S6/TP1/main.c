#include "stack.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define TAGLENGTH 100

enum States { State0,
              State1,
              State2,
              State3,
              State4,
              State5 };

int is_correct_sgml(char fileName[]) {
  FILE *pFile;
  char c;
  Stack stack;
  char tagName[TAGLENGTH]; // Name of the tag (div, head...)
  enum States curState = State0;
  int i; // Counter to write in tagName
  bool closing = false;
  bool correct = true;

  stackInit(&stack);

  if (pFile = fopen(fileName, "rt")) {
    while (!feof(pFile) && correct) {
      c = fgetc(pFile);

      switch (curState) {   //Picture of the automaton in the archive to help you understand
      case State0:
        if (c == '<') {
          curState = State1;
          i = 0;
          memset(tagName, 0, TAGLENGTH * sizeof(char)); // Resets the array
          closing = false;
        }
        break;

      case State1:
        if (isalpha(c)) {
          tagName[i] = c;
          i++;
        } else if (c == ' ') {
          curState = State2;
        } else if (c == '>') {
          curState = State3;
        }
        break;

      case State2:
        if (c == '>') {
          curState = State3;
        } else {
          // Stay here and ignore everything
        }
        break;

      case State3:
        if (c == '<') {
          if (!closing) {
            stackPush(&stack, tagName);
          } else {
            if (strcmp(stackTop(&stack), tagName) == 0) {
              stackPop(&stack);
            } else {
              correct = false;
            }
          }
          i = 0;
          memset(tagName, 0, TAGLENGTH * sizeof(char)); // Resets the array
          closing = false;
          curState = State4;
        } else {
          // Do nothing
        }
        break;

      case State4:
        if (c == '/') {
          closing = true;
          curState = State5;
        } else {
          tagName[i] = c;
          i++;
          curState = State1;
        }
        break;

      case State5:
        if (c == '>') {
          curState = State3;
        } else if (isalpha(c)) {
          tagName[i] = c;
          i++;
        }
        break;
      }
    }
    fclose(pFile);
    return correct;
  } else {
    printf("Couldn't open the file\n");
    return -1;
  }
}

int main() {
  int i = is_correct_sgml("fichier.html");
  if(i != -1){
    printf("%sorrect SMGL file\n", i ? "C" : "Inc");
  }
  return 0;
}