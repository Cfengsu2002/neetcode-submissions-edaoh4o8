class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[[1,0], [-1,0], [0, 1], [0, -1]]
        priority_queue=[]
        heapq.heappush(priority_queue, (grid[0][0],0,0))
        visited=set()
        visited.add((0,0))
        while True:
            current_val, row, col = heapq.heappop(priority_queue)
            for drow, dcol in directions:
                new_row, new_col=row+drow, col+dcol
                if not (new_row<0 or new_col<0 or new_row>len(grid)-1 or new_col>len(grid[0])-1 or (new_row, new_col) in visited):
                    heapq.heappush(priority_queue, (max(current_val, grid[new_row][new_col]),new_row,new_col))
                    visited.add((new_row, new_col))
            
            if(row==len(grid)-1 and col==len(grid)-1):
                return current_val