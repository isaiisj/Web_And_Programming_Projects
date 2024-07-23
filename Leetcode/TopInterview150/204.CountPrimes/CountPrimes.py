'''
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Create an array of True values from 0 to n+1
        prime = [True] * (n+1)
        count = 0

        #0 and 1 are not prime numbers
        if n <= 2:
            return count

        #Once we checked the array has more than 2
        prime[0] = prime[1] = False

        #from 2 to square root of n
        for p in range(2,int(n**0.5)+1):  
            #Check the list
            if prime[p]:
                #if the number is prime
                #mark all the multiples of p as not prime
                #starting from p*p to n+1 and step of p
                for i in range(p*p,n,p):
                    prime[i] = False

        #looping through the list from 2 to n+1
        for i in range(2,n):
            if prime[i]:
                #add one to count
                count += 1

        return count #return total of primes found

'''
Time complexity: O(N*log(log(N)))
'''
