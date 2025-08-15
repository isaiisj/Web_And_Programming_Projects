'''

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 .
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). 
If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]

'''

from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:

    # Delcare an empty list of lists of integers 
    triplets: List[List[int]] = []

    # Sort the array 
    nums.sort()
    
    # Iterate the array
    for i in range(len(nums)):

        # If i element is positive means that no pairs
        # can be formed cause b + c = -a
        if nums[i] > 0:
            break
        
        # If we're in the ith item different from first 
        # and the number is the same as i - 1 keep moving
        if i > 0 and nums[i] == nums [i - 1]:
            continue
        
        # Find all pairs [b,c] to form triplets later
        pairs: List[List[int]] = find_triplets_pairs(nums, i+1, -nums[i])

        # Iterate the pairs [b,c] list
        for pair in pairs:
            # Return the current num and the pairs found in a list
            triplets.append([nums[i]] + pair)

    # Return all triplets found
    return triplets

def find_triplets_pairs(nums: List[int], start: int, target: int) -> List[int]:
        
    # Declare an empty list of pairs [b,c]
    pairs: List[List[int]] = []

    # Declare a right pointer and left pointer at the beginning
    # and at the end of the array
    left: int = start
    right: int = len(nums) - 1

    # Iterate while left < right
    while left < right:

        # If pairs equals the target
        if nums[left] + nums[right] == target:
            # Add the pair to the array and move left
            pairs.append([nums[left],nums[right]])
            left += 1

            # To avoid repetition keep moving the left pointer
            # one step until nums[left] and nums[left - 1] is different
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            
        # If sum is greater than target decrease right
        if nums[left] + nums[right] > target:
            right -= 1
            
        # If sum is less than target increase left
        if nums[left] + nums[right] < target:
            left += 1

    # Return the [b,c] pairs
    return pairs


# Time complexity: O(nlog(n)) + O(n*n) = O(n^2)
