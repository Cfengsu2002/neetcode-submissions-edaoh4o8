class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicated_check=set()
        l,r=0,0
        answer=0
        while r<len(s):
            new_letter=s[r]
            # check inside set or not
            while(new_letter in duplicated_check):
                duplicated_check.remove(s[l])
                l+=1
            duplicated_check.add(new_letter)
            answer=max(len(duplicated_check), answer)
            r+=1
        return answer
                




            
            