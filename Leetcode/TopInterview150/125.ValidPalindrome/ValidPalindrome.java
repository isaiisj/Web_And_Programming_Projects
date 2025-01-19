/*

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

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

*/


class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder palindrome = new StringBuilder(s);
        //Remove non alphanumeric
        for(int i = 0; i < palindrome.length(); i++){
            if(!Character.isLetterOrDigit(palindrome.charAt(i))){
                palindrome.delete(i,i+1);
            }
        }
        //Lower and convert to String
        String palindromeString = palindrome.toString().toLowerCase();
        //Remove blank spaces
        palindromeString = palindromeString.replaceAll("\\s","");
        int p1 = 0;
        int p2 = palindromeString.length() - 1;
        //Iterate with two pointers until p1 >= p2
        while (p1 < p2){
            if(palindromeString.charAt(p1) == palindromeString.charAt(p2)){
                p1++;
                p2--;

            }else {
                return false;
            }
        }
        return true;
    }
    
}

// Time complexity: O(n)
