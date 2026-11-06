class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=-1
        queue=deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]==2):
                    queue.append((y,x))
        directions=[[1,0], [-1,0], [0,1], [0,-1]]
        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                for dy, dx in directions:
                    new_y, new_x=y+dy, x+dx
                    if(new_y<0 or new_x<0 or new_y==len(grid) or new_x==len(grid[0])):
                        continue
                    if(grid[new_y][new_x]==1):
                        queue.append((new_y, new_x))
                        grid[new_y][new_x]=2
            count+=1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]==1):
                    return -1
        return count if count!=-1 else 0
            