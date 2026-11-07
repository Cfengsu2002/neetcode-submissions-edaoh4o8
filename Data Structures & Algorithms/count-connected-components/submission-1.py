class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors=defaultdict(set)
        for edge1, edge2 in edges:
            neighbors[edge1].add(edge2)
            neighbors[edge2].add(edge1)
        visited=set()
        def dfs(node1):
            nonlocal visited
            if node1 in visited:
                return
            visited.add(node1)
            for node2 in neighbors[node1]:
                dfs(node2)
            return
        answer=0
        for i in range(n):
            if i not in visited:
                answer+=1
            dfs(i)
        return answer


