class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        visited=set()
        def dfs(y,x):
            nonlocal visited
            if(y<0 or x<0 or y>len(grid)-1 or x>len(grid[0])-1 
            or (y,x) in visited or grid[y][x]=="0"):
                return
            visited.add((y,x))
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
            return
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]=="1" and (y,x) not in visited):

                    dfs(y,x)
                    islands+=1
        return islands
                

