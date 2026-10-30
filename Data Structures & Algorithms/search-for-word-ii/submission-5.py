class Tri_Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create tri_tree
        root = Tri_Node()

        for word in words:
            current = root
            for i in range(len(word)):
                cha = word[i]
                if cha in current.children:
                    current = current.children[cha]
                else:
                    current.children[cha] = Tri_Node()
                    current = current.children[cha]
            current.is_word = True

        ans = []
        visited = set()
        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(y, x, current, current_word):
            nonlocal ans

            for dy, dx in move:
                new_y = y + dy
                new_x = x + dx

                if (
                    new_y < 0
                    or new_x < 0
                    or new_y > len(board) - 1
                    or new_x > len(board[0]) - 1
                    or (new_y, new_x) in visited
                    or board[new_y][new_x] not in current.children
                ):
                    continue

                visited.add((new_y, new_x))
                current_word.append(board[new_y][new_x])

                if current.children[board[new_y][new_x]].is_word:
                    ans.append("".join(current_word))
                    current.children[board[new_y][new_x]].is_word=False
                dfs(new_y, new_x, current.children[board[new_y][new_x]], current_word)

                visited.remove((new_y, new_x))
                current_word.pop()

        for y in range(len(board)):
            for x in range(len(board[0])):
                current=root
                if board[y][x] in root.children:
                    current=root.children[board[y][x]]
                else:
                    continue
                if current.is_word==True:
                    ans.append(board[y][x])
                    current.is_word=False
                visited.add((y,x))
                dfs(y, x, current, [board[y][x]])
                visited.remove((y,x))
        return ans