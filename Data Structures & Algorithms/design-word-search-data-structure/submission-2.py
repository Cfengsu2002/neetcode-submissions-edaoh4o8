class tri_node:
    def __init__(self):
        self.is_word=False
        self.children={}


class WordDictionary:
    def __init__(self):
        self.root=tri_node()

    def addWord(self, word: str) -> None:
        temp_node=self.root
        for i in range(len(word)):
            if word[i] in temp_node.children:
                temp_node=temp_node.children[word[i]]
            else:
                temp_node.children[word[i]]=tri_node()
                temp_node=temp_node.children[word[i]]
        temp_node.is_word=True

    def search(self, word: str) -> bool:
        # have master card
        return_ans=False
        temp_node=self.root
        
        def dfs(cur_node, index):
            nonlocal return_ans
            if(index==len(word)):
                if(return_ans==False):
                    return_ans=cur_node.is_word
                return
            
            char = word[index]
            if(char=='.'):
                for child, node in cur_node.children.items():
                    dfs(node, index+1)
            else:
                if(char in cur_node.children):
                    dfs(cur_node.children[char], index+1)
            return 
        dfs(temp_node, 0)
        return return_ans
