'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

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

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Create left and right pointer
        left: int = 0
        right: int = len(s) - 1

        # Iterate the array while left < right
        while left < right:

            # While left < right and the item is not alphanumeric
            # keep increasing the left pointer
            while left < right and not s[left].isalnum():
                left += 1

            # Whie left < rigth and the item is not alphanumeric
            # keep decreasing the right pointer
            while left < right and not s[right].isalnum():
                right -= 1
            
            # If the items are equal keep moving the pointers
            # any other way return False
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        # Return true if it is a palindrome
        return True
        
    
# Time complexity: O(n)
