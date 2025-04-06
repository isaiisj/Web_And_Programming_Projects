/*

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

*/


class Solution {
    public boolean isSubsequence(String s, String t) {
        // Create two pointers for s and t 
        int p1 = 0;
        int p2 = 0;

        // Get the length of s
        int len = s.length();
        // Count variable to check subsequence
        int count = 0;

        // While there are letters to check in s and t
        while (p1 < s.length() && p2 < t.length()) {
            // Get ith character of s and t
            char c1 = s.charAt(p1);
            char c2 = t.charAt(p2); 

            // If characters are the same 
            if (c1 == c2) {
                // move both pointers and add 1 to count
                p1 += 1;
                p2 += 1;
                count += 1;
            } else {
                // If not keep move p2
                p2 += 1;
            }
        }

        // If count and length of subequence
        // string are not equal
        if (len != count) return false;

        return true;
    }
}
