class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, num):
            while l<=r:
                m=(l+r)//2
                if(nums[m]==num):
                    return m
                elif(nums[m]>num):
                    r=m-1
                else:
                    l=m+1
            return -1
        
        l,r=0, len(nums)-1
        while l < r:
            m=(l+r)//2
            if(nums[m]>nums[r]):
                l=m+1
            else:
                r=m
        print(l)
        pre_left, pre_right, after_left, after_right=0, l,l,len(nums)-1
        return max(-1, binary_search(pre_left, pre_right, target), binary_search(after_left, after_right, target))