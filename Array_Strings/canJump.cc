#include <vector>
#include <iostream>

using namespace std;

bool canJump(vector<int> nums) {
    int max_reach = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (i > max_reach) {
            return false;
        }
        max_reach = std::max(i, nums.at(i)+i);
        if (max_reach >= nums.size() - 1) {
            return true;
        }
    }
    return true;
}

int main() {
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(4);
    cout << canJump(nums) << endl;
    return 0;
}