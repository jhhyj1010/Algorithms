#include <iostream>
#include <vector>

using namespace std;

vector<int> twoNums(vector<int> nums, int target) {
    int l = 0;
    int h = nums.size() - 1;
    vector<int> ret = {-1, -1};
    // int ret[2] = {-1, -1};

    while (l < h) {
        int total = nums.at(l) + nums.at(h);
        if (total == target) {
            ret[0] = l;
            ret[1] = h;
            return ret;
        }
        else if (total < target) {
            l += 1;
        }
        else {
            h -= 1;
        }
    }
    return ret;
}

int main() {
    vector<int> nums = {2,7,11, 15};
    int target = 9;
    for (int i: twoNums(nums, target)) {
        cout << "number " << i << endl;
    }
    return 0;
}