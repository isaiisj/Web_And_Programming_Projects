'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #two pointers at the beginning and at the end
        p1 = 0
        p2 = len(height) - 1

        #Max area at the moment
        max_area = 0

        while p1 < p2:
            #calculate the area 
            #with the min height
            area = min(height[p1],height[p2]) * (p2-p1) # A = b * A

            #check to store the area or not
            if area > max_area:
                max_area = area

            #We move the pointer with minor height
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            
        return max_area

'''
Time complexity: O(n)
'''
