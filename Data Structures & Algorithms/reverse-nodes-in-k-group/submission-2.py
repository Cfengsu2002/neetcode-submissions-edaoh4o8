# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=tracker=ListNode()
        dummy.next=head
        def reverse(head, tail): # one before the current, one after the current
            prev=None
            current=head_next=head.next
            for i in range(k):
                nxt=current.next
                current.next=prev
                prev=current
                current=nxt
                head_next.next=tail
                head.next=prev
                
        for i in range(k):
            head=head.next
        while True:
            reverse(dummy, head)
            if head==None:
                return tracker.next
            for i in range(k):
                head=head.next
                dummy=dummy.next
                if not head and i!=k-1:
                    return tracker.next
        