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


import java.util.ArrayList;
import java.util.HashMap;   
import java.util.Map;       
import java.util.Arrays;  

public class Main {
    public ArrayList<Integer> pair_sum_unsorted(ArrayList<Integer> nums, int target) {

        // Declare an empty hashmap
        Map<Integer,Integer> hashmap = new HashMap<>();

        // Iterate the ArrayList
        for (int i = 0; i < nums.size(); i++) {

            // If the complement exists in the hashmap
            if (hashmap.containsKey(target - nums.get(i))) {
                // Return an ArrayList with the index of target and current value
                return new ArrayList<>(Arrays.asList(hashmap.get(target - nums.get(i)),i));
            } else {
                // Add the ith element and the index
                hashmap.put(nums.get(i),i);
            }
        }

        // If not pair is found return an empty ArrayList
        return new ArrayList<>();
    }
}


// Time complexity: O(n)
