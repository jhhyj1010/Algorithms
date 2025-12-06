#include <iostream>
#include <vector>

using namespace std;

void reverse_nums(vector<int> &nums, int start, int end) {
    while (start < end) {
        int temp = nums.at(start);
        nums.at(start) = nums.at(end);
        nums.at(end) = temp;
        start += 1;
        end -= 1;
    }
}

void rotateArray(vector<int> &nums, int k) {
    int len = nums.size();
    k %= len;
    reverse_nums(nums, 0, len-1);
    reverse_nums(nums, 0, k-1);
    reverse_nums(nums, k, len-1);
    return;
}

int main() {
    vector<int> nums = {1,2,3,4,5,6,7};
    rotateArray(nums, 3);
    cout << "Rotating the array" << endl;
    for (int i: nums) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}