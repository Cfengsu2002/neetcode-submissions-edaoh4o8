class Solution:
    def numDecodings(self, s: str) -> int:
        # for this question I decide to use dp
        n = len(s)
        dp_array = [0] * (n + 1)
        dp_array[n] = 1
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp_array[i] = 0
            else:
                dp_array[i] = dp_array[i+1]
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                    dp_array[i] += dp_array[i+2]
        return dp_array[0]