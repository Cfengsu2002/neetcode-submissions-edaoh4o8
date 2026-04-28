class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ans=0
        visited=set()
        def dfs(y,x):
            nonlocal visited, land_set
            if(y<0 or x<0 or y>=len(grid) or x>=len(grid[0]) or (y,x) in visited or grid[y][x]==0):
                return 0
            
            visited.add((y,x))
            land_set.add((y,x))
            
            return 1 + dfs(y+1,x) + dfs(y-1,x) + dfs(y,x+1) + dfs(y,x-1)

        land_set=set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]==1 and (y,x) not in land_set):
                    area = dfs(y,x)
                    ans = max(ans, area)
        return ans