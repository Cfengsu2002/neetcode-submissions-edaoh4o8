class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for i in range(len(s)):
            if(s[i].isalpha()):
                new_str+=s[i].lower()
            elif(s[i].isdigit()):
                new_str+=s[i]
        l=0
        r=len(new_str)-1
        while(l<=r):
            if(new_str[l]!=new_str[r]):
                return False
            l+=1
            r-=1
        return True