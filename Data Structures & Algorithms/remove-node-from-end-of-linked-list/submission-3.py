# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead to create the gap
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # left is now at the node BEFORE the one we want to delete
        # Delete the node by skipping it
        left.next = left.next.next
        
        return dummy.next