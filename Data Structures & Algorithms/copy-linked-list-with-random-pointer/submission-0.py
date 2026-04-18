"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origin_node_copy_node={None:None}
        cur_node=head
        # copy every single node first
        while(cur_node):
            origin_node_copy_node[cur_node]=Node(cur_node.val)
            cur_node=cur_node.next
        # link every random and next
        cur_node=head
        while(cur_node):
            copy_node=origin_node_copy_node[cur_node]
            copy_node.next=origin_node_copy_node[cur_node.next]
            copy_node.random=origin_node_copy_node[cur_node.random]
            cur_node=cur_node.next
        return origin_node_copy_node[head]
