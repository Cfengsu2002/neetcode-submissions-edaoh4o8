class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map=defaultdict(int)
        l=0
        ans=0
        max_count=0
        for r in range(len(s)):
            window_size=r-l+1
            hash_map[s[r]]+=1
            max_count = max(max_count, hash_map[s[r]])
            while(window_size-max_count>k):
                hash_map[s[l]]-=1
                l+=1
                window_size=r-l+1
            ans=r-l+1
        return max(ans, window_size)
            
        