'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #Create the dict
        dict = {}
    
        #create the index
        index = 0
    
        #review the list
        for i in nums:

            #check if i is in dict and less or equal to k
            if i in dict and abs(dict[i]-index) <= k:
                return True
            else:
                dict[i] = index #add to dict or replace with new index value
                index += 1
        
        return False

'''
Timme complexity: O(n)
'''
