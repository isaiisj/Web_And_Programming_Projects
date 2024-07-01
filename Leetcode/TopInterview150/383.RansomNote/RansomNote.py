'''
Given two strings ransomNote and magazine, return true 
if ransomNote can be constructed by using the letters from 
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #first we create to empty dictionaries
        dict1 = {}
        dict2 = {}

        #proced to fill dict1 with ransomNote
        for i in ransomNote:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        #proced to fill dict2 with magazine
        for j in magazine:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        #proced to see if values in dict1
        #exist in dict 2
        for i in dict1:
            #if the letters and no.lettes in dict1
            #are less or equal than dict2
            if i in dict2 and dict1[i] <= dict2[i]:
                pass
            else:
                return False
            
        return True

'''
Time complexity: O(N + M)
'''
