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
