class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors=defaultdict(set)
        for edge1, edge2 in edges:
            neighbors[edge1].add(edge2)
            neighbors[edge2].add(edge1)
        
        def dfs(node, parent):            
            nonlocal no_cycle, visited
            if node in visited:
                no_cycle=False
                return
            visited.add(node)
            for node2 in neighbors[node]:
                if (node2==parent):
                    continue
                dfs(node2, node)
            return

        for i in range(len(edges)-1,-1,-1):
            visited=set()
            no_cycle=True
            edge1=edges[i][0]
            edge2=edges[i][1]
            neighbors[edge1].remove(edge2)
            neighbors[edge2].remove(edge1)
            dfs(1, -1)
            neighbors[edge1].add(edge2)
            neighbors[edge2].add(edge1)
            if no_cycle==True and len(visited)==len(edges):
                return [edge1, edge2]
