/*

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Initialize two pointers, p1 and p2, to the start of the string
        int p1 = 0;
        int p2 = 0;

        // Create a HashSet to store unique characters
        Set<Character> set = new HashSet<> ();

        // Initialize count to keep track of the longest substring length
        int count = 0;

        // Continue until either pointer reaches the end of the string
        while (p1 < s.length() && p2 < s.length()){
            // Get the character at p2
            char c = s.charAt(p2);
            // If the character is not in the set
            // (it's unique in the current substring)
            if(!set.contains(c)){ 
                // Add the character to the set
                set.add(c);
                // Move p2 to the next character
                p2++;
                // Update count with the maximum of current count and set size
                count = Math.max(count,set.size());
            } else {
                // If the character is already in the set
                // Remove the character at p1 from the set
                set.remove(s.charAt(p1));
                // Move p1 to the next character
                p1++;
            }
        }

        return count;
    }
}

// Time complexity: O(n)
