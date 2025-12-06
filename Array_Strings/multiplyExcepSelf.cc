
#include <iostream>
#include <vector>

using namespace std;

vector<int> productExceptSelf(vector<int> nums) {
    int length = nums.size();
    vector<int> left(length, 0);
    vector<int> right(length, 0);
    vector<int> results(length, 0);
    left.at(0) = 1;
    for (int i = 1; i < length; i++) {
        left.at(i) = left.at(i-1)*nums.at(i-1);
    }

    right.at(length-1) = 1;
    for (int j = length-2; j > -1; j--) {
        right.at(j) = right.at(j+1)*nums.at(j+1);
    }

    for (int k = 0; k < length; k++) {
        results.at(k) = left.at(k)*right.at(k);
    }
    return results;
}

int main() {
    vector<int> nums = {1,2,3,4};
    vector<int> new_nums = productExceptSelf(nums);

    for (int i: new_nums) {
        cout << "products are: \n" << i <<endl;
    }
    return 0;
}