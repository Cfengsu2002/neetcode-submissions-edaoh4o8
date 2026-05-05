class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        prev_cur_map={}
        for i in range(n):
            prev_cur_map[i]=[]
        for edge_one, edge_two in edges:
            prev_cur_map[edge_one].append(edge_two)
            prev_cur_map[edge_two].append(edge_one)

        visited=set()
        def dfs(cur_node):
            nonlocal visited
            if cur_node in visited:
                return 
            visited.add(cur_node)
            for node in prev_cur_map[cur_node]:
                dfs(node)
            return 

        count=0
        for i in range(n):
            if i not in visited:
                count+=1
            dfs(i)
        return count