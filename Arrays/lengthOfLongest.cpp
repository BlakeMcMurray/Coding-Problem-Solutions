#include <iostream>
#include <unordered_map>
using namespace std;

//finds the longest non repeating char substring in s
int lengthOfLongestSubstring(string s){
    int max_count = 0;
    int p_1 = 0;
    int p_2 = 0;
    unordered_map<char,int> map;
    while(p_2 != s.length()){
        if(map.find(s[p_2]) == map.end()){
            map[s[p_2]] = 1 ;
            p_2++;
        }
        else{
            map.erase(s[p_1]);
            p_1++;
        }
        if(map.size() > max_count){
            max_count = map.size();
        }
    }    
    return max_count;
}

int main()
{   

    cout << lengthOfLongestSubstring("aabc") << endl;
    return 0;

}

