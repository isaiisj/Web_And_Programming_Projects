/*

Given an array of integers sorted in ascending order and a target value,
return the indexes of any pair of numbers in the array that sum to the target.
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].

*/


import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public ArrayList<Integer> pair_sum_sorted(ArrayList<Integer> nums, int target) {
        // Assumes numbers is sorted in ascending order
        // Use two pointers to find pair that sums to target

        // Create the left pointer and the right pointer
        int left = 0;
        int right = nums.size() - 1;

        // Iterate the array while left < right
        while (left < right) {

            // Store the current sum
            int summ = nums.get(left) + nums.get(right);

            // If the sum equals the target return the indexes plus one
            if (summ == target){
                return new ArrayList<>(Arrays.asList(left,right));
            }

            // If the sum is less increase left pointer
            if (summ < target){
                left++;
            }

            // If the sum is greater decrease right pointer
            if (summ > target){
                right --;
            }
        }

        // If there are no pairs, return an emprty array
        return new ArrayList<>();
    }
}


// Time complexity: O(n)
