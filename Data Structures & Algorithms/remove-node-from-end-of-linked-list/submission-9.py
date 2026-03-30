class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # if fast is None → remove head
        if not fast:
            return head.next

        # move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete node
        slow.next = slow.next.next

        return head