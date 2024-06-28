def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() #convert s to lowercase
        s = ''.join(char for char in s if char.isalnum())
        s = [char for char in s] #make s an array with list comprehension
        i = 0 #first pointer index
        j = len(s) -1 #second pointer index

        #while the first pointer is minor
        #than the second one.
        while (i < j):
            #if the indexes are equal
            if(s[i] == s[j]):
                i = i + 1 #add 1 to i
                j = j - 1 #substract 1 to j
            else:
                return False
        return True
