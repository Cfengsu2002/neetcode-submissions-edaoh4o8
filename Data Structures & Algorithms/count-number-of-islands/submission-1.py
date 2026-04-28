class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        visited=set()
        def dfs(y,x):
            nonlocal visited,land_set
            if(y<0 or x<0 or y>=len(grid) or x>=len(grid[0]) or (y,x) in visited or grid[y][x]=='0'):
                return
            visited.add((y,x))
            land_set.add((y,x))
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
            return



        is_land=0
        land_set=set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]=='1' and (y,x) not in land_set):
                    is_land+=1
                    dfs(y,x)
        return is_land