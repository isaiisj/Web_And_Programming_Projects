/*

You are given an array of numbers, each representing the height of a vertical line on a graph.
A container can be formed with any pair of these lines, along with the x-axis of the graph. 
Return the amount of water which the largest container can hold.

Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24

*/


import java.util.ArrayList;

public class Main {
    public int largest_container(ArrayList<Integer> heights) {

        // Delcare left and right pointer
        int left = 0;
        int right = heights.size() - 1;

        // Initial max water
        int maxWater = 0;

        // While left < right continue
        while (left < right) {

            // Get the current area (Base * height)
            int currArea = Math.min(heights.get(left),heights.get(right)) * (right - left);

            // Get max current area
            maxWater = Math.max(currArea,maxWater);

            // If left is < right increase left
            if (heights.get(left) < heights.get(right)){
                left++;
            // If left is > right decrease right
            } else if (heights.get(left) > heights.get(right)){
                right--;
            // Both are equal and move inwards both
            } else {
                right--;
                left++;
            }
        }

        // Return max mater
        return maxWater;

    }
}


// Time complexity: O(n)
