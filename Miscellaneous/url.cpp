#include <unordered_map>
#include <functional>
#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>


int openURL(std::string& url)
{
    std::string command = "start firefox \"" + url + "\"";
    return system(command.c_str());
}


int AmiAmi(std::vector<std::string>& args)
{
    std::string url = "https://www.amiami.com/eng/";
    std::vector<std::string> realURL;
    int nArgs = args.size();
    bool preowned = false, allItems = false;
    if (!nArgs) return openURL(url);

    for (auto& e : args) {
        if (e == "-P") preowned = true;
        else if (e == "-A") allItems = true;
        else realURL.push_back(e);
    }

    if (realURL.size() == 0) {
        std::cerr << " *** Missing search query." << std::endl;
        return 0;
    }

    url += "search/list/?s_keywords=" + realURL.at(0);
    realURL.erase(realURL.begin());
    for (auto& e : realURL) url += ' ' + e;
    if (!allItems) url += "&s_cate_tag=14";
    if (preowned) url += "&s_st_condition_flg=1";

    return openURL(url);
}


int YouTube(std::vector<std::string>& args)
{
    std::string url = "https://www.youtube.com";
    return openURL(url);
}


int Anime(std::vector<std::string>& args)
{
    std::string url = "https://aniwave.to/";
    int nArgs = args.size();
    
    if (nArgs == 0) { url += "user/watch-list?folder=1&keyword"
                             "=&sort=recently_watched"; return openURL(url); }
    url += "filter?keyword=";
    for (int i = 0; i < nArgs - 1; ++i) url += args.at(i) + '+';
    url += args.at(nArgs - 1);
    return openURL(url);
}


int AniList(std::vector<std::string>& args)
{
    std::string url = "https://anilist.co/", type = "search/anime?search=";
    int nArgs = args.size();

    if (nArgs == 0) { url += "user/Ryoon/"; return openURL(url); }
    if (args[0] != "-A" && args[0] != "-M") {
        std::cerr << " *** Missing/incorrect search switch. [-a/-m]" << std::endl;
        return 0;
    }
    if (nArgs == 1) { std::cerr << "*** Missing search query."; return 0; }
    if (args[0] == "-M") type = "search/manga?search=";

    url += type;
    for (int i = 1; i < nArgs - 1; ++i) url += args.at(i) + '+';
    url += args.at(nArgs - 1);

    return openURL(url);
}


int MangaDex(std::vector<std::string>& args)
{
    std::string url = "https://mangadex.org/";
    int nArgs = args.size();
    if (nArgs == 0) { url += "titles/feed"; return openURL(url); }
    url += "search?q=";
    for (int i = 0; i < nArgs - 1; ++i) url += args.at(i) + '+';
    url += args.at(nArgs - 1);
    return openURL(url);
}

// E:\cmder\uni\env url.cpp ::--help::
int Help(std::vector<std::string>& args)
{
    std::string helpStr =
        "\n Keys list :: {Short-hand}\n\n"
        " MangaDex  :: {Manga}\n"
        "     EMPTY :: MangaDex feed page.\n"
        "     TITLE :: Manga title to search.\n\n"
        " AmiAmi    ::\n"
        "     EMPTY :: AmiAmi homepage.\n"
        "     TITLE :: Search figure.\n"
        "  -p TITLE :: Pre-owned search.\n"
        "  -a TITLE :: All search.\n\n"
        " Anilist   ::\n"
        "     EMPTY :: AniList userpage.\n"
        "  -a TITLE :: Anime title search.\n"
        "  -m TITLE :: Manga title search.\n\n"
        " YouTube   :: {YT}\n"
        "     EMPTY :: Open YouTube homepage.";
    std::cout << helpStr << std::endl;
    return 0;
}


std::unordered_map<std::string,
                   std::function<int(std::vector<std::string>&)>> createMap()
{
    std::unordered_map<std::string,
                       std::function<int(std::vector<std::string>&)>> fMap;

    fMap["Mangadex"] = MangaDex;
    fMap["Anilist"] = AniList;
    fMap["Youtube"] = YouTube;
    fMap["Manga"] = MangaDex;
    fMap["Amiami"] = AmiAmi;
    fMap["--Help"] = Help;
    fMap["--List"] = Help;
    fMap["Anime"] = Anime;
    fMap["Yt"] = YouTube;

    return fMap;
}


void titleCase(char* str)
{
    bool upper = true;
    for (char* c = str; *c != '\0'; ++c)
    {
        if (std::isalpha(*c)) {
            if (upper) {
                *c = std::toupper(*c);
                upper = false;
            }
            else { *c = std::tolower(*c); }
        }
        else { upper = true; }
    }
}


int validateArgs(int argc, char* argv[])
{
    if (argc <= 1) {
        std::cerr << " *** No arguments passed." << std::endl;
        return 0;
    }
    for (int i = 1; i < argc; ++i) titleCase(argv[i]);

    std::vector<std::string> postArgs;
    auto funcMap = createMap();

    if (!funcMap.count(argv[1])) {
        std::cerr << " *** Invalid Key: " << argv[1] << std::endl;
        return 0;
    }
    for (int i = 2; i < argc; ++i) postArgs.push_back(argv[i]);
    return funcMap[argv[1]](postArgs);
}


int main(int argc, char* argv[]) { return validateArgs(argc, argv); }
