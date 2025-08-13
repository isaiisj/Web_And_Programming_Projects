/*

Reverse a singly linked list.

1 -> 2 -3 -> 4

     to

4 -> 3 -> 2 -> 1

*/


import { ListNode } from './ds.js'
/**
 * Definition of ListNode:
 * class ListNode {
 *     constructor(val = null, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

export function linked_list_reversal(head) {

  // Declare two pointers at head and null
  let prev = null, curr = head;

  // While we have not reached the end of the list continue
  while (curr != null) {
    // Store the next node before break the link
    let nextNode = curr.next;
    // Reverse the link of the node
    curr.next = prev

    // Move forward prev and curr
    prev = curr;
    curr = nextNode;
  }

  // Return the new head which is the last node
  return prev;
}
