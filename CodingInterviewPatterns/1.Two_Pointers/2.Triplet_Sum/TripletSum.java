/*

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 .
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates).
If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]

*/


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;

public class Main {
    public ArrayList<ArrayList<Integer>> triplet_sum(ArrayList<Integer> nums) {
        
        // Delcare an empty ArrayList
        ArrayList<ArrayList<Integer>> triplets = new ArrayList<>();

        //Sort the array
        Collections.sort(nums);

        // Iterate over the array List
        for (int i = 0; i < nums.size(); i++){

            // Check there ares still pairs to make
            if (nums.get(i) > 0){
                break;
            }

            // Check if value of a is different
            if (i > 0 && nums.get(i) == nums.get(i - 1)){
                continue;
            }

            // Store the list of [b,c] pairs
            List<List<Integer>> pairs = findTripletPairs(nums, i + 1, -nums.get(i));

            // make [a,b,c] triplets and put in the arraylist
            for(List<Integer> list: pairs){
                ArrayList<Integer> triplet = new ArrayList<>();
                triplet.add(nums.get(i));
                triplet.addAll(list);
                triplets.add(triplet);
            }

        }

        // Return all the triplets
        return triplets;

    }

    public static List<List<Integer>> findTripletPairs(ArrayList<Integer> nums, int start, int target){

        List<List<Integer>> pairsFound = new ArrayList<>();

        // Declare left and right pointer
        int left = start;
        int right = nums.size() - 1;

        while (left < right){
            
            // If pairs equals the target
            if (nums.get(left) + nums.get(right) == target){
                pairsFound.add(Arrays.asList(nums.get(left),nums.get(right)));
                left++;

                // While left - 1 is different from left keep moving
                while ( left < right && nums.get(left) == nums.get(left - 1)){
                    left++;
                }
            }

            // If pairs > target decrease right
            if (nums.get(left) + nums.get(right) > target){
                right--;
            }

            // if pairs < target
            if (nums.get(left) + nums.get(right) < target) {
                left++;
            }
        }

        return pairsFound;
    }
}
