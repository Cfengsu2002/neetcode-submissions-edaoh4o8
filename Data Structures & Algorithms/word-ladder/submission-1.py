class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        word_dictionary=defaultdict(list)        
        for word in wordList:
            for i in range(len(word)):
                template = word[:i]+'*'+word[i+1:]
                word_dictionary[template].append(word)
        print(word_dictionary)

        count = 0
        word_queue=deque([beginWord])
        word_visited=set(beginWord)
        while(word_queue):
            count+=1

            for i in range(len(word_queue)):
                current_word=word_queue.popleft()
                if(current_word==endWord):
                    return count
                for i in range(len(current_word)):
                    template = current_word[:i]+'*'+current_word[i+1:]
                    for word in word_dictionary[template]:
                        if(word not in word_visited):
                            word_visited.add(word)
                            word_queue.append(word)
        return 0


