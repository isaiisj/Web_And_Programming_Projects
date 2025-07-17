/*

A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters.
A character is alphanumeric if it's either a letter or a number.

Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True

Example 2:
Input: s = 'abc123'
Output: False

Constraints:
The string may include a combination of lowercase English letters, numbers, spaces, and punctuations.

*/


class Main {
    public Boolean is_palindrome_valid(String s) {
        
        // Create left and right pointer 
        int left = 0;
        int right = s.length() - 1;

        // Iterate the string while left < right
        while (left < right) {

            // while left pointer item is non alphanumeric keep increasing
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // while right pointer item is non alphanumeric keep decreasing
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // If the left and right pointer items are the same 
            // move both pointers other way return false
            if (s.charAt(left) == s.charAt(right)){
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


// TIme complexity: O(n)
