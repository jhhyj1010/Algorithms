#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int maxArea(vector<int> height) {
    int l = 0;
    int r = height.size() - 1;
    int max_vol = std::abs(r - l) * std::min(height.at(l), height.at(r));

    while (l < r) {
        if (height.at(l) < height.at(r)) {
            l += 1;
        }
        else {
            r -= 1;
        }
        max_vol = std::max(max_vol, std::abs(r - l)*std::min(height.at(l), height.at(r)));
    }
    return max_vol;
}

int main() {
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    cout << "Max volume is " << maxArea(height) << endl;
    return 0;
}