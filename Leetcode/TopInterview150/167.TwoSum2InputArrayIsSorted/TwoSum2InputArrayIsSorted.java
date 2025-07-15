/*

Given a 1-indexed array of integers numbers that is already
sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added
by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

*/


class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Assumes numbers is sorted in ascending order
        // Use two pointers to find pair that sums to target

        // Create the left pointer and the right pointer
        int left = 0;
        int right = numbers.length - 1;

        // Iterate the array while left < right
        while (left < right) {

            // Store the current sum
            int summ = numbers[left] + numbers[right];

            // If the sum equals the target return the indexes plus one
            if (summ == target){
                return new int[] {left + 1, right + 1};
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
        return new int[] {};
    }
}


// Time complexity: O(n)
