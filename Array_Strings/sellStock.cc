#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int> prices) {
    int min_price = prices.at(0);
    int max_profit = 0;

    for (int p : prices) {
        min_price = std::min(p, min_price);
        int profit = p - min_price;
        max_profit = std::max(profit, max_profit);
    }
    return max_profit;
}

int main() {
    vector<int> stocks_prices = {7,1,5,3,6,4};
    cout << "Max profit is: " << maxProfit(stocks_prices) << endl;
    return 0;
}