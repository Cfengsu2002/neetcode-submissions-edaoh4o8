# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        input_one=""
        input_two=""
        l1_ptr=l1
        l2_ptr=l2
        str_answer=""
        while l1_ptr:
            input_one=str(l1_ptr.val)+input_one
            l1_ptr=l1_ptr.next
        while l2_ptr:
            input_two=str(l2_ptr.val)+input_two
            l2_ptr=l2_ptr.next
        str_answer=str(int(input_one)+int(input_two))
        dummy=ListNode()
        dummy.next=l1
        for i in range(len(str_answer)-1,-1,-1):
            if(dummy.next==None):
                dummy.next=ListNode()            
            dummy.next.val=str_answer[i]
            dummy=dummy.next
        return l1

        