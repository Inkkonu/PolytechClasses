#include "CFile.h"
#include "FullStackException.h"
#include "NoElementException.h"

unsigned int CFile::GetSize() {
	if (FirstIndex == -1) {
		return 0;
	}
	if (FirstIndex == LastIndex) {
		return 1;
	}
	//From https://stackoverflow.com/a/8026883
	return FirstIndex > LastIndex ? (MaxSize - FirstIndex + LastIndex + 1) : (LastIndex - FirstIndex + 1);
}

CFile& CFile::operator<(const int& v) {
	if (GetSize() != MaxSize) {
		LastIndex++;
		Tab[LastIndex] = v;
		if (FirstIndex == -1) { //If the file was empty
			FirstIndex = 0;
		}
	}
	else {
		throw FullStackException();
	}
	return (*this);
}

CFile& CFile::operator>(int& v) {
	if (GetSize() != 0) {
		v = Tab[FirstIndex];
		if (GetSize() == 1) {
			FirstIndex = -1;
			LastIndex = -1;
		}
		else {
			FirstIndex = (FirstIndex + 1) % MaxSize;
		}
	}
	else {
		throw NoElementException();
	}
	return (*this);
}