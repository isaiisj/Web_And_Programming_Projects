'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color 1  and one of color 2 . There are three odd socks left, one of each color. The number of pairs is  2.

Returns: int - the number of pairs
'''
def sockMerchant(n, ar):
    noPairs = 0 #Start the count in 0
    sock_counts = {} #Create a dict for the numbers and repetitions   number : times 
    for i in ar: 
        if i in sock_counts: #Check if it is in the dict
            sock_counts[i] += 1 #add one to the times it appears
            if sock_counts[i] % 2 == 0: #Check if times is 2n
                noPairs += 1 #Add one pair more 
        else: #If not put it in the dict and it will be the first time 
            sock_counts[i] = 1
    return noPairs
