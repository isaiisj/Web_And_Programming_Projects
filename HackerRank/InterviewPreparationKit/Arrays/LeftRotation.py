'''
A left rotation operation on an array shifts each of the array's 
elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5], 
then the array would become [3,4,5,1,2]. 
Note that the lowest index item moves to the highest index in a rotation. 
This is called a circular array.
Given an array a of n integers and a number, d , perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.
'''
def rotLeft(a, d):
    a1 = a[0:d] #slice array from 0 to d-1
    a2 = a[d:] #slice array from d-1 to the end
    return a2 + a1 #return the to slices interchanged wich would be the equivalent of a rotation
