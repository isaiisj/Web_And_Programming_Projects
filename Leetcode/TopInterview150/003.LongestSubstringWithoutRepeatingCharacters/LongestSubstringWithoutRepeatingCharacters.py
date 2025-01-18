'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a 
subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #create a set or could be a dictionary
        set1 = set()

        #Two poiters at the beginning
        p1 = 0
        p2 = 0

        #store the max length
        maxLen = 0

        #continue while p1 and p2 < len(s) or p1 and p2 <= len(s) - 1
        while p2 < len(s) and p1 < len(s):
          
            #add the letter if not in set, store max length and move p2
            if s[p2] not in set1:
                set1.add(s[p2])
                maxLen = max(maxLen, len(set1))
                p2 += 1
              
            else:
                #remove the las letter and move p1 if repeated is found
                set1.remove(s[p1])
                p1 += 1
            
        return maxLen

'''
Time complexity O(n)
'''
