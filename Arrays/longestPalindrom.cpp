#include <iostream>
#include <unordered_map>
using namespace std;

//checks if string is palindrome
bool check_pal(string s){
    for(int i = 0; i < s.length()/2; i++){

        if(s[i] != s[s.length()-1-i]){
            return false;
        }
    }
    return true;
}



//given string s, finds longest palindromic substring
//O(n^2) solution
string longest_palindrome(string s){
    string l_pal = s.substr(0,1);
    string sub = "";
    for(int i = 0; i < s.length(); i++){
        for(int j = i; j < s.length(); j++){
            sub = s.substr(i,j-i+1); 
            if(check_pal(sub) && sub.length() > l_pal.length()){
                l_pal = sub;
            }
        }
    }
    return l_pal;
}


int main()
{   
    cout << longest_palindrome("abjckdkjeopidjfjeodldabcdcbajdkeoksjsdkfnknlskn") << endl;
    return 0;

}