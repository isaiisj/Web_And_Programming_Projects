'''
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
     
        # empty hashset
        triplets_hashset = set()

        # sort the array
        nums.sort()

        # iterate the array until length - 2
        for i in range(len(nums)-2):

            # Declare two pointers  starting
            # at i + 1 and length - 1
            p1 = i+1
            p2 = len(nums) - 1

            # while p1 < p2 
            while p1 < p2:
                # check if sum equals zero
                if nums[i] + nums[p1] + nums[p2] == 0:
                    # if so add to hashset a tuple and move two pointers
                    triplets_hashset.add((nums[i],nums[p1],nums[p2]))
                    p1 += 1
                    p2 -= 1

                # if it is grater move p2 to the left
                elif nums[i] + nums[p1] + nums[p2] > 0:
                    p2 -= 1

                # if it is less move p1 to the right
                elif nums[i] + nums[p1] + nums[p2] < 0:
                    p1 += 1

        # delcare an empty list
        triplets_list = []
        # convert each tuple into a list and add to the list
        for element in triplets_hashset:
            triplets_list.append(list(element))
            
        return triplets_list
