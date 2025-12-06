#include <iostream>
#include <vector>
#include <set>


using namespace std;

int removeDuplicates(vector<int> nums) {
    std::set<int> uniq_nums;
    int index = 0;

    for (int i : nums) {
        if (!uniq_nums.count(i)) {
            nums.at(index) = i;
            uniq_nums.insert(i);
            index += 1;
        }
    }
    return index;
}

int main() {
    vector<int> numbers = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    cout << removeDuplicates(numbers) << endl;
    return 0;
}