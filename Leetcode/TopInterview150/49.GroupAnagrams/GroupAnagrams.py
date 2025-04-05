'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Create an empty dictionary and list
        mydict = {}
        mylist = []

        # Iterate the array of stirngs
        for string in strs:
            # sort the ith string 
            sorted_text = ''.join(sorted(string))

            # If the string is in dict1
            if sorted_text in mydict:
                # add the unsorted string to the list
                mydict[sorted_text].append(string)
            else:
                # if not add sorted key and add the string to a list
                mydict[sorted_text] = [string]

        # Iterate the hashmap
        for key, value in mydict.items():
            # add each value to the empty list
            mylist.append(value)

        return mylist

# Time complexity: O(k * N * log(N))
