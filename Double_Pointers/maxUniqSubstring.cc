#include <iostream>
#include <string>
#include <set>

using namespace std;

int maxUniqSubstring(string str) {
    set<char> s1 = {};
    int l = 0;
    int max_len = 0;

    for (int i=0; i < str.length(); i++) {
        while (s1.count(str[i])) {
            l += 1;
            s1.erase(str[i]);
        }
        s1.insert(str[i]);
        max_len = std::max(max_len, i-l+1);
    }
    return max_len;
}

int main() {
    string str = "pwwkew";
    cout << maxUniqSubstring(str) << endl;
    return 0;
}