class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # match pair, sort
        nums_index=[]
        for i in range(len(nums)):
            nums_index.append([nums[i], i])
        nums_index.sort()
        # two pointer solution
        l_ptr=0
        r_ptr=len(nums) - 1
        #[[num,index]]
        while l_ptr<r_ptr:
            l_r_sum=nums_index[l_ptr][0]+nums_index[r_ptr][0]
            left_index, right_index=min(nums_index[l_ptr][1], nums_index[r_ptr][1]), max(nums_index[l_ptr][1], nums_index[r_ptr][1])
            if(l_r_sum==target):
                return [left_index, right_index]
            if(l_r_sum>target):
                r_ptr-=1
            else:
                l_ptr+=1
        
        