class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree_map=defaultdict(list)
        for node1, node2 in edges:
            tree_map[node1].append(node2)
            tree_map[node2].append(node1)
        for key, val in tree_map.items():
            if not val:
                return False
        visited=set()
        is_true=True
        def dfs(prev, node,current_visiting):
            nonlocal visited,is_true
            if node in visited:
                return
            if node in current_visiting:
                is_true=False
                return
            current_visiting.add(node)
            for val in tree_map[node]:
                if val == prev:
                    continue
                dfs(node, val, current_visiting)
            current_visiting.remove(node)
            visited.add(node)
            return  
        dfs(-1, 0, set())
        return is_true and len(visited) == n