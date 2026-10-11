class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashset=defaultdict(int)
        for i in range(len(s1)):
            single=s1[i]
            s1_hashset[single]+=1
        print(s1_hashset)

        l=0
        s2_hashset=defaultdict(int)
        count=0
        for r in range(len(s2)):
            s2_hashset[s2[r]]+=1
            count+=1
            if(count>len(s1)):
                count-=1
                s2_hashset[s2[l]]-=1
                if(s2_hashset[s2[l]]==0):
                    del s2_hashset[s2[l]]
                l+=1
            if(s2_hashset==s1_hashset):
                return True
        return False