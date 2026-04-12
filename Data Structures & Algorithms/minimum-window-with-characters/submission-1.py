class Solution:
    def minWindow(self, s: str, t: str) -> str:
        index_list=[0]*100
        for i in range(len(t)):
            index_list[ord(t[i])-ord('A')]+=1
        l=0
        s_index_list=[0]*100
        ans=""
        r=0
        while r<=len(s)-1:
            s_index_list[ord(s[r])-ord('A')]+=1
            while(all(s_index_list[i]>=index_list[i] for i in range(100))):
                if(ans=="" or len(ans)>len(s[l:r+1])):
                    ans=s[l:r+1]
                s_index_list[ord(s[l])-ord('A')]-=1
                print(s[l:r+1])
                l+=1
            r+=1

        return ans
