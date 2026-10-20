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
        node_copy={}
        # copy
        if head == None:
            return None
        copy=head
        while copy:
            node_copy[copy]=Node(copy.val, None, None)
            copy=copy.next
        copy=head
        while copy:
            if(copy.next in node_copy):
                node_copy[copy].next=node_copy[copy.next]
            else:
                node_copy[copy].next=None
            if(copy.random in node_copy):
                node_copy[copy].random=node_copy[copy.random]
            else:
                node_copy[copy].random=None
            copy=copy.next
        return node_copy[head]
