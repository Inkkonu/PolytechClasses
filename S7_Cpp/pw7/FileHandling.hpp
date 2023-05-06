#pragma once

#include <stdlib.h>
#include <string>
#include <iostream>

class FileHandling
{
private:
	struct DirListStruct;
	typedef DirListStruct* DIRHANDLE;
	enum class ETypeResult
	{
		FILE_DIR,
		ONLY_FILE,
		ONLY_DIR
	};

public:
	FileHandling(const char* baseDir);
	FileHandling(const std::string& s) : FileHandling(s.c_str()) {}
	virtual ~FileHandling();
	inline bool GetNext(std::string& str) { return(GetNextElmt(str, ETypeResult::FILE_DIR)); }
	inline bool GetNextFile(std::string& str) { return(GetNextElmt(str, ETypeResult::ONLY_FILE)); }
	inline bool GetNextDir(std::string& str) { return(GetNextElmt(str, ETypeResult::ONLY_DIR)); }

public:
	static bool isFile(const char* file);
	static bool isDir(const char* file);
	static void ParseFileName(const char* const file, std::string& dir, std::string& fileName, std::string& ext);
	static size_t GetFileSize(const char* const file);

private:
	FileHandling(const FileHandling& obj) {}
	FileHandling& operator=(const FileHandling& obj) { return(*this); }
	bool GetNextElmt(std::string& str, ETypeResult kind);

private:
	DIRHANDLE hDir;
};

template <int I = 0, int Limit = 0, class F>
void IterateOnFileDir(const char* baseDir, F&& func)
{
	std::string fileName;

	FileHandling dirList(baseDir);
	int i = 0;
	while ((Limit == 0 || i < Limit) && dirList.GetNextFile(fileName))
	{
		std::string file(baseDir);
		file += fileName;

		func(file.c_str());
		++i;
		if (I != 0 && i % I == 0)
		{
			std::cout << i << " fichier";
			if (i > 1) std::cout << 's';
			std::cout << " traité";
			if (i > 1) std::cout << 's';
			std::cout << std::endl;
		}
	}
}
