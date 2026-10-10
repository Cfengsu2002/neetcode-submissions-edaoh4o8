class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            while(left<len(s)-1 and not (s[left].isalpha() or(s[left].isdigit()))):
                left+=1
            while(right>=0 and not (s[right].isalpha() or(s[right].isdigit()))):
                right-=1

            if(s[left].lower()!=s[right].lower()):
                return False
            left+=1
            right-=1
        return True