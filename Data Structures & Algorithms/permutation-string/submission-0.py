
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash_map=defaultdict(int)
        s2_hash_map=defaultdict(int)
        for character in s1:
            s1_hash_map[character]+=1
        print(s1_hash_map)
        r_ptr=0
        l_ptr=0
        while(r_ptr<=len(s2)-1):
            s2_hash_map[s2[r_ptr]]+=1
            while(r_ptr-l_ptr+1>len(s1) and s2_hash_map!=s1_hash_map):
                s2_hash_map[s2[l_ptr]]-=1
                if(s2_hash_map[s2[l_ptr]]==0):
                    del s2_hash_map[s2[l_ptr]]
                l_ptr+=1
            if(s2_hash_map==s1_hash_map):
                return True
            print(s2_hash_map)
            print(s1_hash_map)
            r_ptr+=1
        return False