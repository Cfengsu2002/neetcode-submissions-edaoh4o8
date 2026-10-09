class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1={}
        map_2={}
        # ord(), int()
        for i in range(26):
            map_1[i+ord('a')]=0
            map_2[i+ord('a')]=0
        # size not equal
        if(len(s)!=len(t)):
            return False

        for i in range(len(s)):
            map_1[ord(s[i])]+=1
            map_2[ord(t[i])]+=1
        print(map_1)
        print(map_2)
        return True if(map_1==map_2) else False