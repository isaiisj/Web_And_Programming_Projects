'''
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #create an empty dict
        dict_nums = {}

        #iterate trough the nums list
        for i,n in enumerate(nums):
            complement = target - n   #obtain complement to target
            if complement in dict_nums:   #if we have the compliment in dict_nums
                return [i, dict_nums[complement]]
            else:
                dict_nums[n] = i   #else add number and  its index array
        
#Time complexity: O(n)
