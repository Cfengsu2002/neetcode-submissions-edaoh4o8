
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_map={}
        visited=set()
        queue=deque([node])
        while queue:
            cur_node=queue.popleft()
            node_map[cur_node]=Node(cur_node.val)
            visited.add(cur_node)
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
        queue=deque([node])
        visited=set()
        while queue:
            cur_node=queue.popleft()
            visited.add(cur_node)
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    node_map[cur_node].neighbors.append(node_map[neighbor])
                    node_map[neighbor].neighbors.append(node_map[cur_node])

        return node_map[node]
