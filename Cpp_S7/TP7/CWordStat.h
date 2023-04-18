#pragma once
#include <map>
#include <string>
#include <regex>
#include <fstream>
#include <vector>
#include <iostream>

class CWordStat
{
public:
	CWordStat() = default;
	CWordStat(const CWordStat& m) = default;
	CWordStat(CWordStat&& m) = default;
	~CWordStat() = default;
	CWordStat& operator=(const CWordStat& m) = default;
	CWordStat& operator=(CWordStat&& m) = default;

	void operator()(const char* file);
	void operator()(const std::string& line, unsigned int lineNumber, unsigned int wordNumber, const std::string& word);

	std::vector<std::string> order();
	void GenerateStopWords();

private:
	std::map<std::string, unsigned int> stats;
};

template<typename F>
void ExtractWords(const char* file, F&& func) {
	std::regex pattern(R"#(\w[\w\-]*)#");
	std::ifstream is;
	is.open(file);
	unsigned int lineNumber = 0;
	unsigned int wordNumber = 0;
	for (std::string line; std::getline(is, line); lineNumber++) {
		std::sregex_iterator begin = std::sregex_iterator(line.begin(), line.end(), pattern);
		std::sregex_iterator end = std::sregex_iterator();

		for (std::regex_iterator i = begin; i != end; ++i) {
			wordNumber++;
			std::smatch match = *i;
			std::string match_str = match.str();
			std::transform(match_str.cbegin(), match_str.cend(), match_str.begin(), ::tolower);
			func(line, lineNumber, wordNumber, match_str);
		}
	}
}