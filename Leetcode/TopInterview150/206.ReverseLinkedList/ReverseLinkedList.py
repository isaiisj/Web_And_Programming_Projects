'''
Given the head of a singly linked list, reverse the list,
and return the reversed list.

Example 1:
1 -> 2 -> 3 -> 4 -> 5

5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:
1 -> 2

2 -> 1

Input: head = [1,2]
Output: [2,1]


Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # if head is null return empty list
        if head is None:
            return head

        # temp points to head
        temp = head
        # after points to head.next
        after = head.next
        # before points to null
        before = None

        # while temp is not null
        while temp:
            # after points to temp.next
            after = temp.next
            # temp.next points to before
            temp.next = before
            # before points to temp
            before = temp
            # temp points to after
            temp = after
        
        # change head where before is ponting at
        head = before

        return head


'''
    Start:  head -> 1 -> 2 -> 3 - null
    End: null <- 1 <- 2 <- 3 <- head
'''
    
# Timpe complexity: O(n)
