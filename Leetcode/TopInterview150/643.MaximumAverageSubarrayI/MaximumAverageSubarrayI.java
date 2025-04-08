/*

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

*/


class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        // two pointers at the beginning
        int p1 = 0;
        int p2 = 0;
        // sum accumulator
        int sumElem = 0;
        // max sum varibale
        int maxSum = 0;
      
        // Add elements until we have k 
        // slide the window and update max sum
        for(int i = 0; i < k;i++){
            sumElem += nums[i];
            maxSum = sumElem;
            p2++;
        }

        // If we have not reache the end of array
        while(p2 < nums.length) {
            // move the window which is the act of
            // substracting left and adding right
            sumElem -= nums[p1];
            sumElem += nums[p2];

            // If the sum obtainded is grater than the
            // one we have update it
            if(sumElem > maxSum){
                maxSum = sumElem;
            }

            // move the ponters to have a new window
            p1++;
            p2++;
        }

        // Return average (don´t forget to typecast)
        return (double) maxSum/k;
    }
}

// Time complexity: O(n)
