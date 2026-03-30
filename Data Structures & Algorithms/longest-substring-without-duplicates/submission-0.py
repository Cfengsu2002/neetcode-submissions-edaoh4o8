class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        l=0
        visited=set()
        for r in range(len(s)):
            while(s[r] in visited):
                visited.remove(s[l])
                l+=1
            ans=max(r-l+1, ans)
            visited.add(s[r])
        return ans 