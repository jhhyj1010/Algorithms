#include <iostream>
#include <vector>

using namespace std;

int canCompleteCircuit(vector<int> gas, vector<int> cost) {
    int ans=0, min_s=0, s=0;
    for (int i = 0; i < gas.size(); i++) {
        s += gas.at(i) - cost.at(i);
        if (s < min_s) {
            min_s = s;
            ans = i + 1;
        }
    }
    if (s < 0) {
        return -1;
    }
    else {
        return ans;
    }
}

int main() {
    vector<int> gas, cost;
    gas.push_back(1);
    gas.push_back(2);
    gas.push_back(3);
    gas.push_back(4);
    gas.push_back(5);

    cost.push_back(3);
    cost.push_back(4);
    cost.push_back(5);
    cost.push_back(1);
    cost.push_back(2);
    cout << canCompleteCircuit(gas, cost) << endl;
    return 0;
}