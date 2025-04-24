/*

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
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

*/


class Solution {
    public int maxArea(int[] height) {
        // Declare two pointers at beggining and
        // end of array
        int p1 = 0;
        int p2 = height.length - 1;
        // a max area variable to store updates
        int maxArea = 0;

        // Move pointers from out to the middle
        while (p1 < p2) {
            // get the minor height from two pointers
            int currentHeight = (height[p1] > height[p2])?height[p2]:height[p1];
            // Get the are of the square (area = base * height)
            int currentArea = currentHeight * (p2-p1);
            
            // If current area is mayor than old one update it
            if(currentArea > maxArea){
                maxArea = currentArea;
            }

            // Move pointer with minor height
            if (height[p1] > height[p2]){
                p2--;
            } else {
                p1++;
            }
            
        }

        return maxArea;
    }
}

// Time complexity: O(n)
