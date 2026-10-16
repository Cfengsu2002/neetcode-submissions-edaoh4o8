# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        dummy=ListNode(-1, head)
        slow_ptr=dummy
        fast_ptr=head
        while fast_ptr!=None and fast_ptr.next!=None:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        prev=None
        current=slow_ptr.next
        slow_ptr.next=None
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt


        # prev is the last value, and it is inversed
        # 10->8->6 prev None
        # 2->4 dummy.next None
        list1=dummy.next
        list2=prev
        while(list2):
            list1_next=list1.next
            list2_next=list2.next
            list1.next=list2
            if list1_next is None:
                break

            list2.next=list1_next
            list1=list1_next
            list2=list2_next            
