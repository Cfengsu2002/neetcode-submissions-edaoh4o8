# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)>1:
            next_round=[]
            for i in range(0,len(lists), 2):
                list_1=lists[i]
                if i+1>=len(lists):
                    list_2=None
                else:
                    list_2=lists[i+1]
                next_round.append(self.merge_list(list_1, list_2))
            lists=next_round
        return lists[0] if lists else None
            


    def merge_list(self, list1, list2):
        dummy = ListNode(0, list1)
        prev = dummy
        cur_1 = list1
        cur_2 = list2

        while cur_1 and cur_2:
            if cur_1.val <= cur_2.val:
                prev = cur_1
                cur_1 = cur_1.next
            else:
                next_2 = cur_2.next
                prev.next = cur_2
                cur_2.next = cur_1
                prev = cur_2
                cur_2 = next_2
        prev.next = cur_1 if cur_1 else cur_2
        return dummy.next