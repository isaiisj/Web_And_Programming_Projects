/*

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

*/


class Solution {
    public int maxProfit(int[] prices) {
        // buy pointer
        int p1 = 0;
        // sell pointer
        int p2 = 0;
        // max profit tracker
        int maxProfit = 0;

        // Continue until we've checked all possible selling days
        while (p2 < prices.length){
            // Calculate current profit
            int currentProfit = prices[p2] - prices[p1];

            // If we can make a profit
            if (currentProfit > 0) {
                // update max profit if current is larger
                if (currentProfit > maxProfit) {
                    maxProfit = currentProfit;
                }
                // move ponter to check next day
                p2++;
            } else {
                // if not profit is possible 
                // move p1 to p2 ans start again
                p1 = p2;
                p2 ++;
            }
        }

        // return max profit
        return maxProfit;
    }
}

// Time complexity: O(n)
