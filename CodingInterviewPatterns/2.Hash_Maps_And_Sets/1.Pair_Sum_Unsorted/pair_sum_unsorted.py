'''

Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result.

'''


from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:

    # Delcare new hashmap
    hashmap = {}

    # Iterate the list 
    for i,n in enumerate(nums):

      # If the compliment is in the hashmap
      if target - n in hashmap:
        # return the index of target and current number
        return [hashmap[target-n],i]
      else:
        # Add the number and its index to hashmap
        hashmap[n] = i
    
    # If not pairs found return empty list
    return []
