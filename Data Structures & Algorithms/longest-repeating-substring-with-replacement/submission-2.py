class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters_values=defaultdict(int)
        l,r=0,0
        answer=0
        while r<len(s):
            letters_values[s[r]]+=1
            while(sum(letters_values.values())- max(letters_values.values())>k):
                letters_values[s[l]]-=1
                l+=1
            answer=max(r-l+1, answer)
            r+=1
        return answer
        