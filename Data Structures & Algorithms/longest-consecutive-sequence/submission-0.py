class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        final_count=0
        for num_set in nums_set:
            count=0
            if(num_set+1 in nums_set):
                continue
            else:
                while(num_set in nums_set):
                    num_set-=1
                    count+=1
                    final_count=max(count, final_count)
        return final_count
