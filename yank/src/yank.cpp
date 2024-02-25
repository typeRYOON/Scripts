#include "yank.hpp"


int addEntry() { return system(openFile.c_str()); }
int listArgs()
{
    std::ifstream file(yankList.c_str());
    if (!file.is_open()) {
        std::cerr << " Error :: YankList file IO." << std::endl;
        return 1; 
    }
    std::string line;
    std::stringstream test;
    while (std::getline(file, line, '\n')) {
        test << "\n  :: " << line;
    }
    std::system("cls");
    std::cout << test.str() << std::endl;
    return 0;
}


path_map createMap()
{
    path_map paths;
    std::ifstream file(yankMap.c_str());
    if (!file.is_open()) {
        std::cerr << " Error :: YankMap file IO." << std::endl;
        return {}; 
    }
    std::string line, key, path, ext;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        if (std::getline(ss, key, ',')  &&
            std::getline(ss, path, ',') &&
            std::getline(ss, ext, ','))
        {
            paths[key] = std::make_tuple(path, ext);
        } else {
            std::cerr << " Error :: Invalid line: " << line << std::endl;
        }
    }
    file.close();
    return paths;
}


void lowerARGV(int argc, char* argv[])
{
    if (argc >= 2) {
        std::transform(argv[1], argv[1] + std::strlen(argv[1]), argv[1],
        [](unsigned char c) { return std::tolower(c); });
    }
}


std::string lowercase(const std::string& str)
{
    std::string ret = str;
    for (char& c : ret) { c = std::tolower(c); }
    return ret;
}


std::string getext(char* a)
{
    std::string str_a(a);
    size_t dotPos = str_a.find_last_of('.');

    if (dotPos != std::string::npos && dotPos < str_a.length()) {
        return str_a.substr(dotPos);
    }
    return "";
}


bool containsBackslash(const char* str)
{
    while (*str != '\0')
    {
        if (*str == '\\') {
            return true;
        }
        ++str;
    }
    return false;
}


int validateArgs(int argc, char* argv[])
{
    lowerARGV(argc, argv);
    if (argc != 3) {
        if (argc == 2 && !strcmp(argv[1], "list"))     { return listArgs(); }
        else if (argc == 2 && !strcmp(argv[1], "add")) { return addEntry(); }
        std::cerr << " Error :: Invalid # of arguments :: (" << argc-1 << " != 2)\n";
        return 1;
    }

    path_map paths = createMap();
    if (paths.empty()) { return 1; }

    auto it = paths.find(argv[1]);
    if (it == paths.end()) {
        std::cerr << " Error :: No match for argument passed." << '\n';
        return 1;
    }
    std::tuple<std::string, std::string> matched = it->second;
    std::string passedExt = lowercase(getext(argv[2]));
    if (passedExt != std::get<1>(matched)) {
        std::cout << " Error :: Non matching extentions (case insensitive)"
                  << "\n       :: (\"" << passedExt << "\" != \"" << std::get<1>(matched)
                  << "\")" << '\n';
        return 1;
    }
    if (containsBackslash(argv[2])) {
        std::cout << " Error :: Remove backslashes :: ( \\ )" << '\n';
        return 1;
    }

    std::string dst = std::filesystem::current_path().string() + "\\" + argv[2];
    std::string command = "cp " + std::get<0>(matched) + " " + dst;
    std::system(command.c_str());
    std::cout << " Yanked :: " << std::get<0>(matched) << std::endl;
    return 0;
}


int main(int argc, char* argv[]) { return validateArgs(argc, argv); }