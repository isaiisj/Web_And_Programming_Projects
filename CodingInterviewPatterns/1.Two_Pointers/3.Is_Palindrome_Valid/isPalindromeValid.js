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


export function is_palindrome_valid(s) {
  
  // Create left and right pointer
  let left = 0;
  let right = s.length - 1;

  // Iterate the array while left < right
  while (left < right) {

    // While left < right and the item is not alphanumeric
    // keep increasing the left pointer
    while (left < right && !isAlphanumeric(s[left])){
        left++;
    }

    // While left < right and the item is not alphanumeric
    // keep decreasing the right pointer
    while (left < right && !isAlphanumeric(s[right])) {
        right--;
    }

    // If the items are equal keep moving the pointers
    // any other way return false
    if (s[left] == s[right]) {
        left++;
        right--;
    } else {
        return false
    }

  }

  // Return true if it is a palindrome
  return true
}

// Helper function to check if character is alphanumeric
function isAlphanumeric(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}

// Time complexity: O(n)
