'''
Given an integer array nums, move all 0's to the 
end of it while maintaining the relative order 
of the non-zero elements.

Note that you must do this in-place without making 
a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Create 2 pointers at the beginning and auxiliary variable
        p1 = 0
        p2 = 0
        aux = 0

        #Length of the array
        LArr = len(nums)

        #Lopping till p1 and p2 < len(nums) or <= len(nums) - 1
        while p1 < LArr and p2 < LArr:

            #if i is not 0
            if nums[p2] != 0:
                aux = nums[p1] #store in aux the value inf p1 
                nums[p1] = nums[p2] #put in p1 the p2 value
                nums[p2] = aux #put in p2 what is in aux
                p1 += 1 #move p1
            p2 += 1 #move p2
        
        return 
        
'''
Time complexity: O(n)
'''
