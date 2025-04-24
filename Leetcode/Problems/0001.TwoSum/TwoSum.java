/*

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

*/

class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Create an empty hashmap
        HashMap<Integer,Integer> mapNums = new HashMap<Integer,Integer>();

        //Create an empty array to return
        int[] indexArr = new int[2];

        // Iterate the nums array
        for(int i = 0; i < nums.length; i++){

            // Get complement to equals target
            int complement = target - nums[i];

            // if the complement is in the hashmap
            if (mapNums.containsKey(complement)){

                //add the index of the number and complement to array
                indexArr[0] = i;
                indexArr[1] = mapNums.get(complement);
            }
            // if not add the numner and its index to hashmap
            else{
                mapNums.put(nums[i],i);
            }
        }

        return indexArr;
    }
}

// Time complexity: O(n)
