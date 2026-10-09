import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a map, the index will be the key
        patterns=collections.defaultdict(list)
        for i in range(len(strs)):
            map_key=[0]*26
            for j in range(len(strs[i])):
                # single str
                index=ord(strs[i][j])-ord('a')
                map_key[index]+=1
            patterns[tuple(map_key)].append(strs[i])
        return list(patterns.values())


                