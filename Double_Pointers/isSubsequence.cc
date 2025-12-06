#include <string>
#include <iostream>

using namespace std;

bool isSubstring(string s, string t) {
    if (s.length() == 0) {
        return true;
    }
    int i = 0;
    for (char c : t) {
        if (c == s[i]) {
            i += 1;
            if (i == s.length()) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    string s = "abc";
    string t = "adfdfbjijoc";
    bool ret = isSubstring( s,  t);
    if (ret) {
        cout << s << " is the substring of " << t << endl;
    }
    else {
        cout << s << " is NOT the substring of " << t << endl;
    }
    return 0;
}