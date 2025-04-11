'''
Given an unsorted array of integers nums, return the length of
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Turn array into hashet
        hashset = set(nums)

        # variable to store max subsequence
        max_count = 0

        # Iterate the hashset (it's randomly arranged)
        for i in hashset:
            # If n-1 is in the hashset means that the current
            # number is not the start of the sequence so skip it
            # but if n-1 is not in hashset let's review next ones
            if i-1 not in hashset:
                # count numbers in subsequence
                count = 0
                # store current value
                curr = i
                # while current number is in hashset
                while curr in hashset:
                    # count 1
                    count += 1
                    # add one to current to search in hashset
                    curr += 1
                
                # if count is grater than the current max
                # update the value
                if count > max_count:
                    max_count = count

        
        return max_count
        
# Time complexity: O(n)
