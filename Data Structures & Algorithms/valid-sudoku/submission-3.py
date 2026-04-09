class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(len(board)):
            print(board[y])
                
        for i in range(len(board)):
            row_visited=set()
            col_visited=set()
            for j in range(9):
                if(board[i][j]!='.' and board[i][j] in row_visited):
                    return False
                if(board[j][i]!='.' and board[j][i] in col_visited):
                    return False
                row_visited.add(board[i][j])
                col_visited.add(board[j][i])
        hash_map=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    continue
                y_index=i//3
                x_index=j//3
                if(board[i][j] in hash_map[(y_index,x_index)]):
                    return False
                hash_map[(y_index,x_index)].append(board[i][j])

        return True