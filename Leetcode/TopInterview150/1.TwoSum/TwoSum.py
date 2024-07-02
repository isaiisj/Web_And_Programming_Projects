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
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #create an empty dict
        dict1 = {}

        #iterate trough the nums list
        for i,n in enumerate(nums):
            complement = target - n   #obtain complement to target
            if complement in dict1:   #if we have the compliment in dict
                return [i, dict1[complement]]
            else:
                dict1[n] = i   #else add and go to the next number
        
#Time complexity: O(n)
