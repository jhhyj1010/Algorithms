#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

bool isPalindrome(string str) {
    str.erase(std::remove_if(str.begin(), str.end(), [](char c) {
        return !std::isalnum(c);
    }), str.end());
    for (char &c : str) {
        c = tolower(c);
    }

    int i = 0;
    int j = str.length() - 1;
    while (i < j) {
        if (str.at(i) != str.at(j)) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    return true;
}

int main() {
    string str = "A man, a plan, a canal: Panama";
    cout << "The input string is " << isPalindrome(str) << endl;
    return 0;
}