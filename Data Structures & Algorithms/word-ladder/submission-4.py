class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # beginWord = "cat" 
        # endWord = "sag"
        # wordList = ["bat","bag","sag","dag","dot"]
        # same length, lower case, distinct
        # "cat" -> "bat" -> "bag" -> "sag".
        # output: 4
        # goal: beginWord -> endWord
        # 1. one different character
        # 2. as many times as needed
        # return minumum transformation
        words_map=defaultdict(set)
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i,len(wordList)):
                for z in range(len(wordList[0])):
                    word1=wordList[i]
                    word2=wordList[j]
                    if(word1[:z]+word1[z+1:] == word2[:z]+word2[z+1:]):
                        words_map[word1].add(word2) #z+1在切片中不会出现问题
                        words_map[word2].add(word1)
                        break 
                        # timecomplexity(m*n*z^2)
        queue=deque([beginWord])
        count=1
        visited=set()
        while queue:
            count+=1
            for i in range(len(queue)):
                current_word=queue.popleft()
                for neighbor in words_map[current_word]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    if neighbor == endWord:
                        return count
                visited.add(current_word)
        return 0
        # count=1 cat
        # count=2 bat
        # count=3 bag
        # count=4 sag return 4


