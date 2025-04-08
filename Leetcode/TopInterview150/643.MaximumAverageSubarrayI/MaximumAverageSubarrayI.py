'''

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

'''


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # pointers at 0
        p1 = 0
        p2 = 0

        # Accumulator for sum
        sum_elem = 0
        # variable for max sum
        max_sum = 0

        # Add numbers until we reach k 
        # for now that is the max sum
        for i in range(0,k):
            sum_elem += nums[i]
            max_sum = sum_elem
            p2 += 1

        # If p2 has not reached the end of array
        while p2 < len(nums):
            # substract left element
            sum_elem -= nums[p1]
            # add right element
            sum_elem += nums[p2]
            # this is equivalent to slide the window

            # update max_sum if we have a new max
            if sum_elem > max_sum:
                max_sum = sum_elem

            # slide the window (move pointers)
            p1 += 1
            p2 += 1

        # In python 3 it's not nescessary to typecast
        # it throws a float by itself
        return float(max_sum)/float(k)

# Time complexity: O(n)
