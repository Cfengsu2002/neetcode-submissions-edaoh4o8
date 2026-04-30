class Solution:
    def solve(self, board: List[List[str]]) -> None:
        new_board=[['O']* (len(board[0])+2) for row in range(len(board)+2)]
        
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                new_board[1+y][1+x]=board[y][x]
        
        visited=set()
        def dfs(y,x):
            nonlocal new_board
            if(y<0 or x<0 or y>=len(new_board) or x>=len(new_board[0]) or(y, x) in visited):
                return
            if(new_board[y][x]=='X'):
                return
            if(new_board[y][x]=='O'):
                new_board[y][x]='marked'
            visited.add((y,x))
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
            return 
        dfs(0,0)
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if(board[y][x]==new_board[y+1][x+1]):
                    board[y][x]='X'

        for row in board:
            print(row)

