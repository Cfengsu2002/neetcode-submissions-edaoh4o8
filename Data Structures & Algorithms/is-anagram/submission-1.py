class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map=defaultdict(int)
        t_map=defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]]+=1
        for i in range(len(t)):
            t_map[t[i]]+=1
        return True if(t_map==s_map) else False 
        

