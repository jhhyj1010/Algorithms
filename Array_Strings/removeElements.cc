#include <vector>
#include <iostream>

using namespace std;

int removeElements(vector<int> nums, int value) {
    int count = 0;
    for (int i: nums) {
        if (i != value) {
            nums.at(count) = i;
            count += 1;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {0,1,2,2,3,0,4,2};
    int value = 2;
    cout << removeElements(nums, value) << endl;
    return 0;
}