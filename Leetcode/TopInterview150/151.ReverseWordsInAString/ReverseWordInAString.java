/*
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
*/

public class ReverseWords {
    public static void main(String[] args) {
        System.out.println(reverseWord("Hola Mundo"));
    }

    public static String reverseWord( String s){
        //Split the phrase by word in an array
        String[] word = s.split("\\s+"); //O(n)
     
        //Create empty string
        StringBuilder reverse = new StringBuilder(""); //O(1)
     
        //Iterate word array starting from end to start
        for (int i = word.length - 1; i >= 0; i--) { //O(n)
            //Append each word in our empty string
            reverse.append(word[i]);//O(n)
            reverse.append(" ");
        }
     
        //Trim the reverse string
        return reverse.toString().trim(); //O(n)
    }
}

/*
If we use a string builder we avoid to use extra memory
* */


//Time complexity: n + 1 + 2n + n = 4n + 2 = n
//Space complexity: O(n)
