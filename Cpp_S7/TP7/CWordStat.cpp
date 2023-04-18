#include "CWordStat.h"
#include <fstream>

void CWordStat::operator()(const char* file) {
	ExtractWords(file, *this);
}

void CWordStat::operator()(const std::string& line, unsigned int lineNumber, unsigned int wordNumber, const std::string& word)
{
	auto s = stats.find(word);
	if(s != stats.end()){
		stats[word]++;
	}
	else {
		stats[word] = 1;
	}
}

std::vector<std::string> CWordStat::order() {
	std::vector<std::string> v = {};
	for (std::map<std::string, unsigned int>::iterator it = stats.begin(); it != stats.end(); ++it) {
		v.push_back(it->first);
	}
	std::sort(v.begin(), v.end(), [&](std::string s1, std::string s2) {
		return stats[s1] > stats[s2];
		});

	return v;
}

void CWordStat::GenerateStopWords() {
	std::vector<std::string> v = this->order();
	std::ofstream outfile("stopWords.txt");
	unsigned int size = stats.size();
	for (unsigned int i = 0; i < size / 100; i++) {
		outfile << v[i] << std::endl;
	}
	for (unsigned int i = size / 5; i < size; i++) {
		outfile << v[i] << std::endl;
	}
	outfile.close();
}
