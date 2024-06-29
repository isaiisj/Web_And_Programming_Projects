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
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() #convert s to lowercase
        s = ''.join(char for char in s if char.isalnum()) #make a new array without alphanumeric 
        s = [char for char in s] #make s an array with list comprehension, an alternative list(s)
        i = 0 #first pointer index
        j = len(s) - 1 #second pointer index

        #while the first pointer is minor
        #than the second one.
        while (i < j):
            #if the last and first indexes are equal
            if(s[i] == s[j]):
                i = i + 1 #add 1 to i #move the first poiter to right
                j = j - 1 #substract 1 to j #move the second one to left
            else:
                return False
        return True
