/*

Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

*/


class Solution {
    public void moveZeroes(int[] nums) {

        // two pointers at the beginning
        int p1 = 0;
        int p2 = 0;

        // while there are numbers 
        while(p1 < nums.length && p2 < nums.length){

            // if p2 is not zero 
            if (nums[p2] != 0){

                // store p2 in aux
                // put p2 in p1
                // put aux in p2
                int aux = nums[p2];
                nums[p2] = nums[p1];
                nums[p1] = aux;
                p1++;
            }
          
            p2++;
        }
    }
}

// Time complexity: O(n)
