#include <iostream>
#include <map>
#include <vector>


using namespace std;

int removeDuplicatesII(vector<int> nums) {
    int stack_size = 2;
    for (int i = 2; i < nums.size(); i++) {
        if (nums.at(i) != nums.at(stack_size - 2)) {
            nums.at(stack_size) = nums.at(i);
            stack_size += 1;
        }
    }
    return std::max(stack_size, static_cast<int>(nums.size()));
}

int removeDuplicatesII_map(vector<int> nums) {
    map<int, int> num_occurrence;
    int index = 0;
    for (int n: nums) {
        if ((! num_occurrence.count(n)) || (num_occurrence.count(n) && num_occurrence.count(n) < 2)) {
            num_occurrence[n] += 1;
            nums.at(index) = n;
            index += 1;
        }
    }
    return index;
}

int main() {
    vector<int> nums = {0, 0, 1, 1, 1, 1, 2, 3, 3};
    cout << removeDuplicatesII_map(nums) << endl;
    return 0;
}