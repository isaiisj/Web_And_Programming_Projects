/*

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next pointer references an earlier node
in the linked list, causing a loop.

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

class Main {
    public static Boolean linked_list_loop(ListNode<Integer> head) {
        
        // Delcare fast and slow pointers
        ListNode slow = head, fast = head;

        // While fast and fast.next continue
        while (fast != null && fast.next != null) {

            // Move one step slow
            slow = slow.next;
            // Move two steps fast
            fast = fast.next.next;

            // If slow == fast there's a loop
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}


// Time complexity: O(n)
