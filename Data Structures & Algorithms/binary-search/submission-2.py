class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr=0
        right_ptr=len(nums)-1
        while left_ptr<=right_ptr:
            middle_ptr=(left_ptr+right_ptr)//2
            if(nums[middle_ptr]==target):
                return middle_ptr
            elif(nums[middle_ptr]>target):
                right_ptr=middle_ptr-1
            else:
                left_ptr=middle_ptr+1
        return -1