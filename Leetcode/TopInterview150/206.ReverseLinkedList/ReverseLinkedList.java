/*

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

*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {

        // after points to head
        ListNode after = head;
        // before points in null
        ListNode before = null;
        // temp points to head
        ListNode temp = head;

        // while temp points to not null node
        while(temp != null){

            // after points to temp.next
            after = temp.next;
            // temp.next points to before
            temp.next = before;
            // before points to temp
            before = temp;
            // temp points to after
            temp = after;

        }

        // change head pointer where before is pointing at
        head = before;

        return head;
    }
}

/*
    Start:  head -> 1 -> 2 -> 3 - null
    End: null <- 1 <- 2 <- 3 <- head
*/

// Time complexity: O(n)
