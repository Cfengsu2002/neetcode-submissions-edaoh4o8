class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()

        for i in range(len(nums)):
            target=-nums[i]
            l=i+1
            r=len(nums)-1
            while(l<r):
                if(nums[l]+nums[r]<target):
                    l+=1
                elif(nums[l]+nums[r]>target):
                    r-=1
                else:
                    ans.add((-target, nums[l],nums[r]))
                    l+=1
                    r-=1
        return list(list(element) for element in ans)
