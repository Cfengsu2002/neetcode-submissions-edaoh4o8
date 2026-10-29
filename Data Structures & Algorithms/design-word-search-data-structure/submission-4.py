class Tri_Node:
    def __init__(self):
        self.is_word=False
        self.children={}

class WordDictionary:

    def __init__(self):
        self.root=Tri_Node()

    def addWord(self, word: str) -> None:
        current=self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                current.children[word[i]]=Tri_Node()
            current=current.children[word[i]]
        current.is_word=True
    def search(self, word: str) -> bool:
        def dfs(index, current_node):
            if index==len(word):
                return current_node.is_word
            if word[index]!='.' and word[index] not in current_node.children:
                return False
            if word[index]=='.':
                for key, value in current_node.children.items():
                    if dfs(index+1, value):
                        return True
                return False
            else:
                current_node=current_node.children[word[index]]
                return dfs(index+1, current_node)
            return current_node.is_word
        return dfs(0, self.root)
            



