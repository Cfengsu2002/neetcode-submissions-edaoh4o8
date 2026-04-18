# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node_l1=l1
        l1_str=""
        while(cur_node_l1):
            l1_str=str(cur_node_l1.val)+l1_str
            cur_node_l1=cur_node_l1.next
        l1_int=int(l1_str)
        cur_node_l2=l2
        l2_str=""
        while(cur_node_l2):
            l2_str=str(cur_node_l2.val)+l2_str
            cur_node_l2=cur_node_l2.next
        l2_int=int(l2_str)
        l3_str=str(l1_int+l2_int)
        is_head=False
        head=None
        temp=head
        print(l3_str)
        for i in range(len(l3_str)-1,-1,-1):
            cur_cha=l3_str[i]
            if(is_head==False):
                is_head=True
                temp=head=ListNode(int(cur_cha))
            else:
                temp.next=ListNode(int(cur_cha))
                temp=temp.next
        return head

        