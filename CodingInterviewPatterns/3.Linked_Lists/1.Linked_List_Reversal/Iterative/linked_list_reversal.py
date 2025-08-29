'''

Reverse a singly linked list.

1 -> 2 -> 3 -> 4

       to

4 -> 3 -> 2 -> 1

'''


from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:
    
    # Create an extra pointer to head and to null
    curr, prev = head, None

    # While we haven't reached the end of the list
    while curr:

        # Save the next node before we break the link
        next_node: ListNode = curr.next
        # Reverse the pointer of current node
        curr.next = prev

        # Move prev and curr one step forward
        prev = curr
        curr = next_node
    
    # Return the new head which is the last node
    return prev


# Time complexity: O(n)
