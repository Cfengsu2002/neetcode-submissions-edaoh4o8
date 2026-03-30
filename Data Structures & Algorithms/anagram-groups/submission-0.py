class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_set=defaultdict(list)
        for word in strs:
            word_key=[0]*26
            for single_cha in word:
                single_index=ord(single_cha)-ord('a')
                word_key[single_index]+=1
            answer_set[tuple(word_key)].append(word)
        ans=[]
        for element in answer_set.values():
            ans.append(element)
        return ans 
