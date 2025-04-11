/*

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

*/


class Solution {
    public int longestConsecutive(int[] nums) {
        // check first if leng is not 0
        if (nums.length == 0) return 0;

        int maxCount = 0;
        // Declare empty hashset
        Set<Integer> set = new HashSet ();

        // Fill the hashset
        for(int num: nums){
            set.add(num);
        }

        // Iterate hashset
        for (int num: set){
            int count = 0;
            int curr = num;
            // If n-1 not in hashtet start to count 
            if (!set.contains(curr-1)){
                // while n+1 exists add 1 to count and number
                while (set.contains(curr)){
                    count++;
                    curr++;
                }
            }

            // update max subsequence number 
            maxCount = Math.max(count,maxCount);
        }

        return maxCount;
    }
}

// Time complexity: O(n)
