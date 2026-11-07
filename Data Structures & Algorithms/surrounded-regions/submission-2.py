class Solution:
    def solve(self, board: List[List[str]]) -> None:
        new_grid=[["O"]*(len(board[0])+2) for i in range(len(board)+2)]
        for y in range(len(board)):
            for x in range(len(board[0])):
                new_grid[y+1][x+1]=board[y][x]

        visited=set()
        def dfs(y,x):
            nonlocal visited
            if (y,x) in visited:
                return
            if (y<0 or y>=len(new_grid) or x<0 or x>=len(new_grid[0])):
                return
            if(new_grid[y][x]=="X"):
                return
            visited.add((y,x))
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
            return
        dfs(0,0)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if((y+1, x+1) in visited):
                    continue
                else:
                    board[y][x]="X"
