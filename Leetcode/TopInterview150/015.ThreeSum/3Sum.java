/*

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

*/


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // HashSet to store unique triplets (automatically handles duplicates)
        Set<List<Integer>> set = new HashSet<>();

        // Sort array to use two-pointer technique
        Arrays.sort(nums);

        // Iterate through array, fixing first number of triplet
        for(int i = 0; i < nums.length; i++){
            // Two pointers: p1 starts after i, p2 starts at end
            int p1 = i+1;
            int p2 = nums.length - 1;
            // Use two-pointer technique to find pairs that sum with nums[i] to zero
            while(p1 < p2) {
                int sum  = nums[i] + nums[p1] + nums[p2];
                if(sum == 0){
                    // Found a triplet that sums to zero
                    set.add(Arrays.asList(nums[i],nums[p1],nums[p2]));
                    p1++;
                    // Skip duplicates for p1 to avoid duplicate triplets
                    while((p1 < p2) && nums[p1] == nums[p1-1]){
                        p1++;
                    }
                } else if (sum > 0){
                    // Sum too large, decrease p2 to reduce sum
                    p2--;
                } else{
                    // Sum too small, increase p1 to increase sum
                    p1++;
                }
            }
        }

        // Convert Set to List for return value
        List<List<Integer>> res = new ArrayList<>();
        for(List<Integer> list: set){
            res.add(list);
        }

        return res;

    }
}

// Time complexity: O(n)
