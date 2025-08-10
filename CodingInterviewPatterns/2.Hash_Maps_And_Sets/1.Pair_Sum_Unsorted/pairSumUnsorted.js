/*

Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result.

*/


export function pair_sum_unsorted(nums, target) {

  // Create an empty hashmap
  const hashmap = new Map();

  // Iterate the array
  for (let i = 0; i < nums.length; i++) {

    // If the complement exists in the hasmap
    if (hashmap.has(target - nums[i])) {

        // Return the index of complement and index of current number
        return [hashmap.get(target - nums[i]),i];
    } else {

        // Else add the current number and index
        hashmap.set(nums[i],i);
    }
  }

  // If not pair is found return an empty array
  return []  

}


// Time complexity: O(n)
