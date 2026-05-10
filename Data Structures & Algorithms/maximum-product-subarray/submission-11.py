class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_big_num=-float('inf')
        temp_small_num=1
        temp_big_num=1
        for i in range(len(nums)):
            print(nums[i], temp_small_num*nums[i], temp_big_num*nums[i])
            prev=temp_big_num
            temp_big_num=max(nums[i], temp_small_num*nums[i], temp_big_num*nums[i])
            temp_small_num=min(nums[i], prev*nums[i], temp_small_num*nums[i])
            final_big_num=max(final_big_num, temp_big_num)
        return final_big_num