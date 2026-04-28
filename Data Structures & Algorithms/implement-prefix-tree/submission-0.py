class prefix_node:
    def __init__(self):
        self.children={}
        self.is_word=False



class PrefixTree:

    def __init__(self):
        self.root=prefix_node()

    def insert(self, word: str) -> None:
        cur_ptr=self.root
        for i in range(len(word)):
            if(word[i] in cur_ptr.children):
                cur_ptr=cur_ptr.children[word[i]]
            else:
                new_node=prefix_node()
                cur_ptr.children[word[i]]=new_node
                cur_ptr=cur_ptr.children[word[i]]
        cur_ptr.is_word=True


    def search(self, word: str) -> bool:
        cur_ptr=self.root
        for i in range(len(word)):
            if(word[i] in cur_ptr.children):
                cur_ptr=cur_ptr.children[word[i]]
            else:
                return False
        return cur_ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        cur_ptr=self.root
        for i in range(len(prefix)):
            if(prefix[i] in cur_ptr.children):
                cur_ptr=cur_ptr.children[prefix[i]]
            else:
                return False
        return True        