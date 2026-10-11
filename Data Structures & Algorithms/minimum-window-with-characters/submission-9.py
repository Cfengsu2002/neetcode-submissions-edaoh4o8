class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern=Counter(t)
        pattern_size=len(pattern)
        pattern_match=0
        s_pattern=defaultdict(int)
        ans_l, ans_r=0, float('inf')
        l=0
        if(len(s)<len(t)):
            return ""
        for r in range(len(s)):
            s_pattern[s[r]]+=1
            if(s[r] in pattern and s_pattern[s[r]]==pattern[s[r]]):
                pattern_match+=1
            while(pattern_match==pattern_size):
                if(ans_r-ans_l+1>r-l+1):
                    ans_r, ans_l=r,l
                s_pattern[s[l]]-=1
                if(s[l] in pattern and s_pattern[s[l]]<pattern[s[l]]):
                    pattern_match-=1
                l+=1
        return "" if ans_r == float('inf') else s[ans_l: ans_r+1]