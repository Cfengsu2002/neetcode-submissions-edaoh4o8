class tri_node:
    def __init__(self):
        self.is_word=False
        self.children={}
    
    def add_word(self, word):
        cur_node=self
        for single_cha in word:
            if single_cha in cur_node.children:
                cur_node=cur_node.children[single_cha]
            else:
                new_node=tri_node()
                cur_node.children[single_cha]=new_node
                cur_node=new_node
        cur_node.is_word=True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=tri_node()
        for word in words:
            root.add_word(word)
        ans=set()
        def dfs(y,x, root, cur_word):
            nonlocal visited
            if(y>=len(board) or x>=len(board[0]) or x<0 or y<0):
                return
            if(board[y][x] not in root.children):
                return
            if((y,x) in visited):
                return
            cur_word=cur_word+board[y][x]
            visited.add((y,x))
            if(root.children[board[y][x]].is_word==True):
                ans.add(cur_word)
            dfs(y+1, x, root.children[board[y][x]], cur_word)
            dfs(y-1, x, root.children[board[y][x]], cur_word)
            dfs(y, x+1, root.children[board[y][x]], cur_word)
            dfs(y, x-1, root.children[board[y][x]], cur_word)
            visited.remove((y,x))
            return
        for row in board:
            print(row)
        visited=set()

        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(y, x, root, "")
        return list(ans) 
            
            

