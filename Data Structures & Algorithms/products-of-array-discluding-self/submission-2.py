class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left=[1]*len(nums)
        prefix_right=[1]*len(nums)
        for i in range(len(nums)):
            if(i-1<0):
                prefix_left[i]=1
            else:
                prefix_left[i]=prefix_left[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                prefix_right[i]=1
            else:
                prefix_right[i]=prefix_right[i+1]*nums[i+1]
        answer=[]
        for i in range(len(nums)):
            answer.append(prefix_left[i]*prefix_right[i])
        return answer