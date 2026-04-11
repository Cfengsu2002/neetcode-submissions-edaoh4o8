class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr = 0
        r_ptr = len(nums) - 1

        while l_ptr < r_ptr:
            m_ptr = (l_ptr + r_ptr) // 2
            if nums[m_ptr] > nums[r_ptr]:
                l_ptr = m_ptr + 1
            else:
                r_ptr = m_ptr

        if l_ptr > 0 and nums[0] <= target <= nums[l_ptr - 1]:
            l = 0
            r = l_ptr - 1
        else:
            l = l_ptr
            r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1