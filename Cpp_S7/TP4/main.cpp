#include "CContainer.h"
#include "CFile.h"
#include "CPile.h"

int main() {
	CContainer v(2);
	CPile pile, * pPile;
	CFile file, * pFile;

	v[0] = &pile;
	v[1] = &file;

	pFile = dynamic_cast<CFile*>(v[0]);
	pPile = dynamic_cast<CPile*>(v[1]);

	return 0;
}