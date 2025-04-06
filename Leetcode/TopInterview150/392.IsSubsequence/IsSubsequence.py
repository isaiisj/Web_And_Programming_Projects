'''
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
'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0 #pointer 1 looping s
        j = 0 #pointer 2 looping t
        
        # number of letters in s
        lenInp = len(s) 
        #should find the same nubmer as len(t)
        count = 0 
        
        #While there are letters in s and t to search
        while i < len(s) and j < len(t):
            #if letters are equal
            if s[i] == t[j]:
                i += 1 #move p1 to the right
                j += 1 #move p2 to the right
                count += 1 #count 1
            else:
                j += 1 #just move j
        
        #if count is not the same as lenInp 
        if lenInp != count:
            return False #not all the letters exist and not subset

        return True #otherwise it is subset 
