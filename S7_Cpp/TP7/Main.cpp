#include <locale>
#include <iostream>
#include "FileHandling.hpp"
#include "CWordStat.h"
#include "CIndex.h"

int main() {
	std::locale::global(std::locale("fr-FR")); //To deal with accentuated characters

	//CWordStat statsFR;
	//IterateOnFileDir<100>("./texts/", statsFR);
	//ExtractWords("Main.cpp", statsFR);
	//statsFR.GenerateStopWords();

	CIndex("stopWords.txt");

	return (EXIT_SUCCESS);
}