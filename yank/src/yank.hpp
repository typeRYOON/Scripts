#include <unordered_map>
#include <filesystem>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <fstream>
#include <cstdlib>
typedef std::unordered_map<std::string, std::tuple<std::string, std::string>> path_map;
std::string openFile = "np E:\\cmder\\templates\\YankMap.txt";
std::string yankList = "E:\\cmder\\templates\\YankList.txt";
std::string yankMap  = "E:\\cmder\\templates\\YankMap.txt";