class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find where they turn
        l_ptr=0
        r_ptr=len(nums)-1
        while(l_ptr<r_ptr):
            m_ptr=(l_ptr+r_ptr)//2
            if(nums[m_ptr]>nums[r_ptr]):
                l_ptr=m_ptr+1
            else:
                r_ptr=m_ptr
        return nums[l_ptr]
