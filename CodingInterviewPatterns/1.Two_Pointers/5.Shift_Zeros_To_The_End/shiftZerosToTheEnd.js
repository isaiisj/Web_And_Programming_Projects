/*

Given an array of integers, modify the array in place to move all
zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]

*/


export function shift_zeros_to_the_end(nums) {

  // Create the left pointer
  let left = 0;

  // For loop will work as right pointer
  for (let i = 0; i < nums.length; i++) {

    // If the item is different form 0
    if (nums[i] != 0) {

        // Store the value of right pointer
        let aux = nums[i];

        // Swap the numbers
        // Put in right the left value and 
        // aux in left
        nums[i] = nums[left];
        nums[left] = aux;

        // Increase the left pointer
        left++;
    }
  }
}

// Time complexity: O(n)
