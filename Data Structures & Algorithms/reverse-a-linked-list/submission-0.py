# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        temp_prev=None
        while(temp):
            temp_next=temp.next
            temp.next=temp_prev
            temp_prev=temp
            temp=temp_next
        return temp_prev