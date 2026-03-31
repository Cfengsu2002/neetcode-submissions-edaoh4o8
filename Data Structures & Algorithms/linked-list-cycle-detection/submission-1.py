# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        fast_ptr=head.next
        slow_ptr=head
        while(fast_ptr!=None):
            if(fast_ptr==slow_ptr):
                return True
            if(fast_ptr and fast_ptr.next):
                fast_ptr=fast_ptr.next.next
                slow_ptr=slow_ptr.next
            else:
                return False
        return False
            