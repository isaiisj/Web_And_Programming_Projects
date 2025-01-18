'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Create the stack
        stack = []

        #review the string
        for i in s:
            #for any of these (, {, [
            if i == "(" or i == "{" or i == "[":
                stack.append(i)   #push them in the stack
        
            #if the stack is not empty
            elif len(stack) > 0:
                #review for every closing bracket if the 
                #previous one is the open bracket and pop it
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return stack.append(i)  #if not just put it in the stack
            else:
                stack.append(i)   #if the stack is empty put first something

        #if the final stack is full a missing bracket exists
        if len(stack) != 0:
            return False

        #if is empty, everything is right
        return True  
            
'''
Time complexity: O(n)
'''
