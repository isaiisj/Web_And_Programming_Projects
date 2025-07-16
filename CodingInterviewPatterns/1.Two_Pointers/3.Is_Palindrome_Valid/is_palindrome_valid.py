'''

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

'''


def is_palindrome_valid(s: str) -> bool:   

    # Create left and right pointer 
    left: int = 0
    right: int = len(s) - 1

    # Iterate the array while left < right
    while left < right:
        
        # While left < right and the item is not alphanumeric
        # keep increasing the left pointer
        while left < right and not s[left].isalnum():
            left += 1

        # While left < right and the item is not alphanumeric
        # keep decreasing the right pointer
        while left < right and not s[right].isalnum():
            right -= 1

        # If the items are equal keep moving the pointers
        # any other way return false
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    # Return true if it is a palindrome
    return True


# Time complexity: O(n)
