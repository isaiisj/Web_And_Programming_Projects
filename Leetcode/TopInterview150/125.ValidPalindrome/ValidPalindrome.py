'''
A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same 
forward and backward. Alphanumeric characters include 
letters and numbers.

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

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # convert s to lowercas
        s = s.lower()
        # make a new string without alphanumeric characters
        s = "".join(char for char in s if char.isalnum())

        # create two indexes to iterate the array
        # from start to end and from end to start
        p1 = 0
        p2 = len(s) - 1

        # while p1 < p2
        while p1 < p2:
            # if two characters are no the same
            # return false
            if s[p1] != s[p2]:
                return False
            # Other way keep loking up
            p1 += 1
            p2 -= 1
            
        return True

'''
Time complexity: O(n)
'''
