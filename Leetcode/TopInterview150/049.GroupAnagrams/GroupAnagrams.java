/*

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

*/


class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // Create an empty hashmap and empty Arraylist
        Map<String,ArrayList<String>> map = new HashMap();
        List<List<String>> arrayList = new ArrayList();

        // Iterate through the array
        for(int i = 0; i < strs.length;i++) {

            // Get the ith str
            String unsorted = strs[i];

            // Convert the srt to char array to sort and back
            // again to string
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            // If sorted str is in hashmap
            if(map.containsKey(sorted)) {
                // Get the value and add the unsorted to array
                map.get(sorted).add(unsorted);
            } else {
                // If not add the sorted as key, create a new array
                // and add the first element unsorted str
                map.put(sorted,new ArrayList<>());
                map.get(sorted).add(unsorted);
            }

        }

        // Iterate through the hashmap and get the values to add them to 
        // the array list
        for (Map.Entry<String,ArrayList<String>> entry: map.entrySet()) {
            ArrayList<String> value = entry.getValue();
            arrayList.add(value);
        }

        return arrayList;

    }
}

// Time complexity: O(k * N * log(N))
