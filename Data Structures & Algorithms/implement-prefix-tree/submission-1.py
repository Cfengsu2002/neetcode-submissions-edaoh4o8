class prefixNode:
    def __init__(self):
        self.is_word=False
        self.children={}


class PrefixTree:

    def __init__(self):
        self.root=prefixNode()

    def insert(self, word: str) -> None:
        temp=self.root
        for i in range(len(word)):
            if(word[i] in temp.children):
                temp=temp.children[word[i]]
            else:
                temp.children[word[i]]=prefixNode()
                temp=temp.children[word[i]]
        temp.is_word=True
    def search(self, word: str) -> bool:
        temp=self.root
        for i in range(len(word)):
            if(word[i] in temp.children):
                temp=temp.children[word[i]]
            else:
                return False
        if temp.is_word==True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        temp=self.root
        for i in range(len(prefix)):
            if(prefix[i] in temp.children):
                temp=temp.children[prefix[i]]
            else:
                return False
        return True