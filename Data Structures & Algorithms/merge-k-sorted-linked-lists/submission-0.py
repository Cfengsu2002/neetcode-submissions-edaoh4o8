# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_linked_list_queue=[]
        # if not None, put inside min_linked_list_queue
        i=0
        for linked_list in lists:
            if(linked_list!=None):
                first_value=linked_list.val
                heapq.heappush(min_linked_list_queue, [first_value,i ,linked_list])
            i+=1
        print(min_linked_list_queue)
        
        cur_node=dummy=ListNode()

        while min_linked_list_queue:
            queue_small_value, index, linked_list=heapq.heappop(min_linked_list_queue)
            cur_node.next=linked_list
            cur_node=cur_node.next
            if(linked_list.next):
                heapq.heappush(min_linked_list_queue, [linked_list.next.val,index,linked_list.next])
        return dummy.next
            
