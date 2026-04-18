class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_counts=Counter(nums)
        for num, count in num_counts.items():
            if(count!=1):
                return num
            
