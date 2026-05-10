class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create the dp list
        ans_list=len(s)*['False']
        ans_list.append('True')
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if( i + len(word) <= len(s) and word == s[i:i+len(word)]):
                    if ans_list[i+len(word)] == 'True':
                        ans_list[i] = 'True'
        print(ans_list)
        return True if ans_list[0]=='True' else False