/*

Reverse a singly linked list.

1 -> 2 -> 3 -> 4

      to

4 -> 3 -> 2 -> 1

*/


import core.LinkedList.ListNode;
/**
 * Definition of ListNode:
 * public class ListNode<T> {
 *     T val;
 *     ListNode next;
 *     ListNode(T val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
 
public class Main {
    public static ListNode<Integer> linked_list_reversal(ListNode<Integer> head) {

        // Declare to pointers at null and head
        ListNode<Integer> prev = null, curr = head;

        // While we haven´t reached the last node
        while (curr != null) {
          
            // Save the next node before break the link
            ListNode<Integer> nextNode = curr.next;
            // Reverse the pointer of current node
            curr.next = prev;

            // Move forward prev to curr and curr to next node
            prev = curr;
            curr = nextNode;
        }

        // Return the new head which is last node
        return prev;
    }
}


// Time complexity: O(n)
