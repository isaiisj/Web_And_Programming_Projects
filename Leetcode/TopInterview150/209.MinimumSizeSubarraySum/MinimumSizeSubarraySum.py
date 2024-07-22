'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        #This is solved with sliding window technique

        #Declare two pointers starting at 0
        p1 = 0
        p2 = 0

        #sum of the current subarray
        summ = 0
    
        #len starts at infinity
        lenSubArr = float('inf')

        #Look the array till p2 < lenArr and p1 < lenArr
        while p2 < len(nums) and p1 < len(nums):

            #add the first number
            summ += nums[p2]

            #len of the current subarray
            lenSubArr2 = p2 - p1 + 1

        
            #if the current sum >= target
            if summ >= target:

                #store the current length if is less than the store
                if lenSubArr2 < lenSubArr:
                    lenSubArr = lenSubArr2

                #remove from sum first number
                summ -= nums[p1]
                p1 += 1 #move first pointer
                summ -= nums[p2] #remove from sum last number

            else:
                p2 += 1 #move first pointer

        return lenSubArr if lenSubArr != float('inf') else 0

        '''
        Time complexity: O(n)
        '''
