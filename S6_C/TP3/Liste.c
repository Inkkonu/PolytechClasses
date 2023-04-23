#include "Liste.h"
#include <stdlib.h>
#include <stdio.h>

struct SCell{
  Data value;
  SCell *next;
  SCell *prev;
};

struct SList{
  SCell *head;
  int size;
};

SList* CreateList(){
  SList *list = (SList *) malloc(sizeof(SList));
  list->head = NULL;
  list->size = 0;
  return list;
}

void DeleteList(SList *list){
  if(list->size != 0){
    if(list->size == 1){
      free(list->head);
    }
    else{
      SCell *currentCell = list->head;
      SCell *nextCell = currentCell->next;
      while(nextCell != NULL){
        free(currentCell);
        currentCell = nextCell;
        nextCell = currentCell->next;
      }
      free(currentCell);
    }
  }
  free(list);
}

SCell* AddElementBegin(SList *list, Data elem){
  if(list->size == 0){
    SCell *head = (SCell *) malloc(sizeof(SCell));
    head->value = elem;    
    list->head = head;
    list->size++;
    return head;
  }
  else{
    SCell *previousHead = list->head;
    SCell *newHead = (SCell *) malloc(sizeof(SCell));
    newHead->value = elem;
    newHead->next = previousHead;
    previousHead->prev = newHead;
    list->size++;
    list->head = newHead;
    return newHead;
  }
}

SCell* AddElementEnd(SList *list, Data elem){
  if(list->size == 0){ //If the list is empty, adding at the end is the same as adding at the beginning
    return AddElementBegin(list, elem);
  }
  else{
    SCell *previousTail = GetLastElement(list);
    SCell *newTail = (SCell *) malloc(sizeof(SCell));
    newTail->value = elem;
    newTail->prev = previousTail;
    previousTail->next = newTail;
    list->size++;
    return newTail;
  }
}

SCell* AddElementAfter(SList *list, SCell *cell, Data elem){
  if((list->size == 0) || (cell == NULL)){
    return NULL;
  }
  else{
    SCell *currentCell = list->head;
    while(currentCell != NULL && currentCell != cell){ //Find the cell you passed in parameter in the list
      currentCell = currentCell->next;
    }
    if(currentCell == NULL){ //If the cell isn't in the list, you can't create a new cell
      return NULL;
    }
    if(currentCell->next == NULL){ //If the cell passed in parameter is the tail
      return AddElementEnd(list, elem);
    }
    else{
      SCell *cellToAdd = (SCell *) malloc(sizeof(SCell));
      cellToAdd->value = elem;
      cellToAdd->next = currentCell->next;
      cellToAdd->prev = currentCell;
      currentCell->next = cellToAdd;
      cellToAdd->next->prev = cellToAdd;
      list->size++;
      return cellToAdd;
    }
  }
}

void DeleteCell(SList *list, SCell *cell){
  if(cell != NULL && list->size != 0){
    SCell *currentCell = list->head;
    while(currentCell != NULL && currentCell != cell){ //Find the cell you passed in parameter in the list
      currentCell = currentCell->next;
    }
    if(currentCell != NULL){ //If you found the cell passed in parameter
      if(currentCell->next == NULL){ //If the cell you want to delete is the tail
        currentCell->prev->next = NULL;
	free(currentCell);
      }
      else{
        if(currentCell->prev == NULL){ //If the cell you want to delete is the head
	  currentCell->next->prev = NULL;
	  list->head = currentCell->next;
	  free(currentCell);
	}
	else{ //If it's a "regular" cell
	  currentCell->next->prev = currentCell->prev;
	  currentCell->prev->next = currentCell->next;
	  free(currentCell);
	}
      }
    list->size--;
    }
  }
}

SCell* GetFirstElement(SList *list){
  if(list->size == 0){
    return NULL;
  }
  return list->head;
}

SCell* GetLastElement(SList *list){
  if(list->size == 0){
    return NULL;
  }
  else{
    SCell *cell = list->head;
    for(int i = 0 ; i < list->size-1 ; i++){
      cell = cell->next;
    }
    return cell;
  }
}

SCell* GetPrevElement(SCell *cell){
  return cell->prev;
}

SCell* GetNextElement(SCell *cell){
  return cell->next;
}

Data GetData(SCell *cell){
  return cell->value;
}

