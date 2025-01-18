/*

Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the
same type.
 

Example 1:

Input: s = "()"

Output: true


Example 2:

Input: s = "()[]{}"

Output: true


Example 3:

Input: s = "(]"

Output: false


Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

*/


class Solution {
    public boolean isValid(String s) {

         // Create an arraylist of charaters
        ArrayList<Character> stack = new ArrayList<Character>();

        // iterate through the string
        for (int i = 0; i < s.length(); i++){

            // get each character of the string
            char c = s.charAt(i);

            //If the stack has already something
            if(stack.size() > 0){
                // get last item pushed
                char lp = stack.get(stack.size()-1);
                // if it is ")" or "}" or "]" and last item
                // push it is the opposite remove it
                if (c == ')' && lp == '('){
                    stack.remove(stack.size() - 1);
                }else if(c == '}' && lp == '{'){
                    stack.remove(stack.size() - 1);
                }else if(c == ']' && lp == '['){
                    stack.remove(stack.size() - 1);
                }else{
                    // other case leave it in the stack
                    stack.add(c);
                }
            }else{
                // add something first
                stack.add(c);
            }


        }

        // if we have something that means we have some
        // characters unpaired
        if (stack.size() > 0) return false;

        return true;

    }
}

// Time complexity: O(n)
