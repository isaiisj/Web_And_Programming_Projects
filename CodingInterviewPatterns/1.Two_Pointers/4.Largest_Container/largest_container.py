'''

You are given an array of numbers, each representing the height of a vertical line on a graph. 
A container can be formed with any pair of these lines, along with the x-axis of the graph. 
Return the amount of water which the largest container can hold.

Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24

'''


from typing import List

def largest_container(heights: List[int]) -> int:
    
    # Declare left and right pointer
    left, right = 0, len(heights) - 1

    # Max water
    max_water = 0

    # While left < right continue
    while left < right:

        # Get the current area (base * height)
        area = min(heights[left],heights[right]) * (right - left)

        # Update max current
        if area > max_water :
            max_water = area

        # If left is less move left one
        if heights[left] < heights[right]:
            left += 1
        
        # If left is greater decrease right
        elif heights[left] > heights[right]:
            right -= 1
        
        # If both are equal move both
        else:
            left += 1
            right -= 1
        
    # Return max area of water
    return max_water


# Time complexity: O(n)
