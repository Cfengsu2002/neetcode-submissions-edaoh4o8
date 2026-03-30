class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use dict
        # sort based on dict values
        num_count=defaultdict(int)
        for num in nums:
            num_count[num]+=1
        num_count=sorted(num_count.items(), key=lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(num_count[i][0])
        return ans
