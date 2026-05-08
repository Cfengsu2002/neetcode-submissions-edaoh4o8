class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_str=""
        def find_shortest_palindromic(l,r):
            nonlocal ans_str
            temp_str=""
            while(True):
                if(l<0 or r>=len(s)):
                    break
                if(s[l]!=s[r]):
                    break
                if(l==r):
                    temp_str=s[l]
                else:
                    temp_str=s[l]+temp_str+s[r]
                if(len(temp_str)>len(ans_str)):
                    ans_str=temp_str
                l=l-1
                r=r+1
        for i in range(len(s)):
            if(i>0):
                find_shortest_palindromic(i-1, i)
                find_shortest_palindromic(i,i)
            else:
                find_shortest_palindromic(i,i)
        return ans_str