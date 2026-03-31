# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l_header=list1
        r_header=list2
        three_header=four_header=ListNode()
        while(l_header and r_header):
            if(l_header.val<=r_header.val):
                three_header.next=l_header
                l_header=l_header.next
                three_header=three_header.next
            else:
                three_header.next=r_header
                r_header=r_header.next
                three_header=three_header.next

        while(l_header):
            three_header.next=l_header
            l_header=l_header.next
            three_header=three_header.next

        while(r_header):
            three_header.next=r_header
            r_header=r_header.next
            three_header=three_header.next

        return four_header.next