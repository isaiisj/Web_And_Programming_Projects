'''

Given an array of integers, modify the array in place to move all zeros
to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]

'''

from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:

    # Create left and right pointer at the 
    # beginning of the array
    left: int = 0;

    # Keep moving right pointer until the end
    # (the for loop acts as right pointer)
    for i in range(len(nums)):

        # If the element is different from 0 
        if nums[i] != 0:

            # Next line just applies in python and 
            # aux varible is nedeeded in other languages
            # Swap right for left and left for right
            nums[left],nums[i] = nums[i], nums[left]

            # increment the left pointer
            left += 1


# Time complexity: O(n)
