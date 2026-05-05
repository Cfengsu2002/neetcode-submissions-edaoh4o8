class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes_map={}
        for node in range(n):
            nodes_map[node]=[]
        for edge_one, edge_two in edges:
            nodes_map[edge_one].append(edge_two)
            nodes_map[edge_two].append(edge_one)
        print(nodes_map)
        ans_set=set()
        visited_node=set()
        def dfs(prev_node, cur_node):
            nonlocal visited_node
            if(cur_node in visited_node):
                return False
            visited_node.add(cur_node)
            for next_node in nodes_map[cur_node]:
                if(next_node == prev_node):
                    continue
                if(dfs(cur_node, next_node)==False):
                    return False
            return True
        return True if(dfs(-1, 0) and len(visited_node)==n) else False
        