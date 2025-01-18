'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        #make the number a string to be iterable
        x = str(x)
        #make x a string
        x = list(x)

        #Define two pointers at the beginning and at the end
        p1 = 0
        p2 = len(x) - 1

        #while p1 < p2 if an item is diferent is not a palindrome
        while p1 < p2:
            if x[p1] != x[p2]:
                return False
            p1 += 1
            p2 -= 1
            
        return True

'''
Time complexity: O(n)
'''
