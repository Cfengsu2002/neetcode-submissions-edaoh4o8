"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_copy={}
        if not node:
            return None
        node_copy[node]=Node(node.val)
        queue=deque()
        queue.append(node)
        while queue:
            cur=queue.popleft()
            for nei in cur.neighbors:
                if nei not in node_copy:
                    node_copy[nei]=Node(nei.val)
                    queue.append(nei)
                node_copy[cur].neighbors.append(node_copy[nei])

        return node_copy[node]