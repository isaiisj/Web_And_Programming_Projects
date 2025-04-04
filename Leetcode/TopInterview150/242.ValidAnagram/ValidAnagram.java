/*

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

*/


class Solution {
    public boolean isAnagram(String s, String t) {
        if (t.length() != s.length()) return false;

        // Lower the strings
        s.toLowerCase();
        t.toLowerCase();

        // Delcare to empty hashmaps
        Map<Character,Integer> map1 = new HashMap ();
        Map<Character,Integer> map2 = new HashMap ();

        // Fill first and second hashmap with s and t {character:count}
        // at the same time for not repeating code
        for (int i = 0; i < s.length(); i++) {
            // Get ith character of string
            char cs = s.charAt(i);
            char ct = t.charAt(i);

            // put in the value the current value plus one
            // but if it doesn't exist add it and add one
            map1.put(cs,map1.getOrDefault(cs,0)+1);
            map2.put(ct,map2.getOrDefault(ct,0)+1);
        }

        // Compare two hashmaps (key and value)
        if (map1.equals(map2)) return true;

        return false;
    }
}

// Time complexity O(n)
