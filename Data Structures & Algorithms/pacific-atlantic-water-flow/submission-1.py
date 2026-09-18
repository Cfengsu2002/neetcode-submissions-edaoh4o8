class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_land=set()
        atlantic_land=set()






        def dfs(y,x, land, prev):
            if((y,x) in land):
                return land
            if(y<0 or x<0 or y>len(heights)-1 or x>len(heights[0])-1):
                return land
            if(prev<=heights[y][x]):
                land.add((y,x))
            else:
                return land
            dfs(y+1,x,land, heights[y][x])
            dfs(y-1,x,land, heights[y][x])
            dfs(y,x+1,land, heights[y][x])
            dfs(y,x-1,land, heights[y][x])
            return land

        for y in range(len(heights)):
            dfs(y,0, pacific_land, -float('inf'))
            dfs(y,len(heights[0])-1, atlantic_land,-float('inf'))
        
        for x in range(len(heights[0])):
            dfs(0, x, pacific_land,-float('inf'))
            dfs(len(heights)-1, x, atlantic_land,-float('inf'))
        return list(atlantic_land&pacific_land)
