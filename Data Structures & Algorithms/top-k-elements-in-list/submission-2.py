class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency={}
        for num in nums:
            if num not in nums_frequency:
                nums_frequency[num]=1
            else:
                nums_frequency[num]+=1
        nums_frequency=sorted(nums_frequency.items(), key=lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(nums_frequency[i][0])
        return ans