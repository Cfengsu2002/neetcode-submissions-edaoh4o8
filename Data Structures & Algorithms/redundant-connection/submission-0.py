class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge_map=defaultdict(list)
        def cycle_detect(prev_edge, cur_edge):
            if(cur_edge in visited):
                return False
            visited.add(cur_edge)
            for next_edge in edge_map[cur_edge]:
                if(next_edge==prev_edge):
                    continue
                if(cycle_detect(cur_edge, next_edge)==False):
                    return False
            return True
        for edge_one, edge_two in edges:
            edge_map[edge_one].append(edge_two)
            edge_map[edge_two].append(edge_one)
            visited=set()
            if(cycle_detect(-1,edge_one)==False):
                return [edge_one, edge_two]

        return [-1,-1]