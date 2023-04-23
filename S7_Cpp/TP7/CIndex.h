#pragma once
#include <set>
#include <string>
#include <map>
#include <vector>

class CIndex
{
public:
	CIndex(const char* file);
	~CIndex();

	void operator()(const char* fileName);
	bool operator()(const std::string& line, unsigned int lineNumber, unsigned int wordNumber, const std::string& word);

private:
	std::set<std::string> stopWords;

	class SDoc {
	public:
		std::string fileName;
		std::string title;
		std::map<std::string, unsigned int> wordFrequencies;
		unsigned int numberOfWords;

		SDoc(const char* file) : fileName(fileName) {};
	};

	std::vector<SDoc*> SDocs;
};

