/*

Given an array of integers, modify the array in place to move all
zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]

*/


import java.util.ArrayList;

class UserCode {
    public static void shiftZerosToTheEnd(ArrayList<Integer> nums) {

        // Delcare left pointer
        int left = 0;

        // For loop will work as right pointer
        // going through the ArrayList
        for (int i = 0; i < nums.size(); i++) {

            // If the item is different
            if (nums.get(i) != 0) {

                // Store the item in right pointer
                int aux = nums.get(i);

                // (Swap the numbers) Put the in 
                // right the thing of left
                // and in left the item stored
                nums.set(i,nums.get(left));
                nums.set(left,aux);

                // Increase left pointer
                left++;
            }
        }
    }
}


// Time complexity: O(n)
