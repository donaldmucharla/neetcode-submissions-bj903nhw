# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findKth(groupPrev, k)

            if not kth:
                break
            groupnext = kth.next
            
            cur, prev = groupPrev.next, kth.next
            while cur != groupnext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    
    def findKth(self, cur, k):
        while cur and k>0:
            cur = cur.next
            k -= 1
        
        return cur
        