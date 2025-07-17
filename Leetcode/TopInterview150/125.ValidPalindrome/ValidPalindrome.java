/*

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

*/


class Solution {
    public boolean isPalindrome(String s) {

        // Create left and right pointer 
        int left = 0;
        int right = s.length() - 1;

        // Iterate the string while left < right
        while (left < right) {

            // while left < right anf pointer item is non alphanumeric keep increasing
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // while left < right and item is non alphanumeric keep decreasing
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // If the left and right pointer items are the same 
            // move both pointers other way return false
            if (Character.toString(s.charAt(left)).toLowerCase().equals(Character.toString(s.charAt(right)).toLowerCase())){
                left++;
                right--;
            }else{
                return false;
            }
        }

        // If it is palindrome return true
        return true;

    }
}


// Time complexity: O(n)
