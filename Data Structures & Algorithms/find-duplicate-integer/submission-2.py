class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast_ptr=0
        slow_ptr=0
        while True:
            fast_ptr=nums[nums[fast_ptr]] #trump twice
            slow_ptr=nums[slow_ptr]
            if(slow_ptr==fast_ptr):
                break
        new_slow_ptr=0
        while(new_slow_ptr!=slow_ptr):
            new_slow_ptr=nums[new_slow_ptr]
            slow_ptr=nums[slow_ptr]
        return slow_ptr

            
