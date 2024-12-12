/*

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

*/

class Solution {
    public String reverseVowels(String s) {
        //Transform input String into a StringBuilder
        StringBuilder newString = new StringBuilder(s);

        //Declare vocals as a hash set
        Set<Character> Vocals = new HashSet<>();
        Vocals.add('a');
        Vocals.add('e');
        Vocals.add('i');
        Vocals.add('o');
        Vocals.add('u');
        Vocals.add('A');
        Vocals.add('E');
        Vocals.add('I');
        Vocals.add('O');
        Vocals.add('U');

        //Two pointers at the beginning and at the end
        //of the StringBuilder
        int p1 = 0;
        int p2 = newString.length() - 1;


        //Iterate until p2 >= p1
        while(p1 < p2){


            //If p1 and p2 are vocals
            if(Vocals.contains(newString.charAt(p1)) && Vocals.contains(newString.charAt(p2))){
                //Store in aux variable p1
                char aux = newString.charAt(p1);
                //Replace p2 in p1
                newString.replace(p1,p1+1,Character.toString(newString.charAt(p2)));
                //Put p1 which now is aux in p2
                newString.replace(p2,p2+1,Character.toString(aux));
                //Move the pointers
                p1++;
                p2--;
                continue;
            }
            //p1 vocal but p2 not a vocal
            if(Vocals.contains(newString.charAt(p1)) && !Vocals.contains(newString.charAt(p2))){
                p2--;
                continue;
            }
            //p1 not a vocal but p1 a vocal
            if(!Vocals.contains(newString.charAt(p1)) && Vocals.contains(newString.charAt(p2))){
                p1++;
            }
            //None is a vocal
            else {
                p1++;
                p2--;
            }
        }

        return newString.toString();
    }
}

// Time complexity: O(n)
