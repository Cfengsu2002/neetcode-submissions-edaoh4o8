class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 获得iterative time
        temp_node=head
        total_node_num=0
        while(temp_node!=None):
            temp_node=temp_node.next
            total_node_num+=1
        iterations=total_node_num//k
        dummy=ListNode(-1, head)
        def reverse_subgroup(group_prev, group_after):
            cur_node=group_prev.next
            prev=group_after
            next_start=cur_node
            nxt=cur_node.next
            for i in range(k):
                nxt=cur_node.next
                cur_node.next=prev
                prev=cur_node
                cur_node=nxt
            # next_start.next=nxt  # This was redundant and causing issues
            group_prev.next=prev


        begin_node=dummy        
        for i in range(iterations):
            next_start_node=begin_node
            for _ in range(k):
                next_start_node=next_start_node.next
            end_node=next_start_node.next
            # Save the node that will be the new 'begin_node' for the next iteration
            current_tail = begin_node.next
            reverse_subgroup(begin_node, end_node)
            begin_node=current_tail
        return dummy.next