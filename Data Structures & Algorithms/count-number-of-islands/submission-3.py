class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        def dfs(y, x):
            nonlocal visited
            if y<0 or y>len(grid)-1 or x<0 or x>len(grid[0])-1:
                return
            if (y, x) in visited:
                return
            if grid[y][x]=='0':
                return
            visited.add((y,x))
            dfs(y+1, x)
            dfs(y-1, x)
            dfs(y, x+1)
            dfs(y, x-1)
            return

        count=0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]=='1' and (y, x) not in visited:
                    count+=1
                    dfs(y, x)
        return count