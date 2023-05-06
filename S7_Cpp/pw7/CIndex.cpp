#include "CIndex.h"
#include "CWordStat.h"
#include <iostream>
#include <fstream>

CIndex::CIndex(const char* file) {
	ExtractWords(file, [&](const std::string& line, unsigned int lineNumber, unsigned int wordNumber, const std::string& word) {
		stopWords.insert(word);
		});
	std::cout << stopWords.size() << std::endl;
}

CIndex::~CIndex()
{
	for (SDoc* document : SDocs)
	{
		delete(document);
	}
}

void CIndex::operator()(const char* fileName) {
	std::ifstream file(fileName);
	SDoc* doc = new SDoc(fileName);
	SDocs.push_back(doc);
	ExtractWords(fileName, *this);
	for (auto const& [key, val] : doc->wordFrequencies) {
		doc->wordFrequencies[key] = doc->wordFrequencies[key] / doc->numberOfWords;
	}
}

bool CIndex::operator()(const std::string& line, unsigned int lineNumber, unsigned int wordNumber, const std::string& word) {
	SDoc* doc = SDocs[SDocs.size() - 1]; //Last doc added is the one we're working on if everything works normally
	doc->numberOfWords = wordNumber;
	if (lineNumber == 1) {
		doc->title = line;
	}
	if (lineNumber <= 2) {
		return false;
	}
	else {
		if (!stopWords.contains(word)) {
			if (!doc->wordFrequencies.contains(word)) {
				doc->wordFrequencies[word] = 0;
			}
			doc->wordFrequencies[word]++;
		}
		return true;
	}
}