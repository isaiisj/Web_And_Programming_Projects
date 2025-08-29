'''

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next pointer references an earlier node
in the linked list, causing a loop.

'''


rom ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_loop(head: ListNode) -> bool:
    
    # Declare a slow and fast pointer
    slow = fast = head

    # Iterate while fast and fast.next is not None
    while fast and fast.next:

        # Move one step slow
        slow = slow.next
        # Move two steps fast
        fast = fast.next.next

        # If both coincide there's a loop
        if slow == fast:
            return True
    
    # Return false if there is no a loop
    return False
