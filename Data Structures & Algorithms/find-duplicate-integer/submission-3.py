class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=-1
        slow=-2
        while fast!=slow:
            if(fast==-1 and slow==-2):
                fast=0
                slow=0
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow2=0
        while True:
            if(slow==slow2):
                return slow
            slow=nums[slow]
            slow2=nums[slow2]