class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums2)<len(nums1)):
            nums1, nums2=nums2, nums1
        total_len=len(nums2)+len(nums1)
        half_len=total_len//2


        nums1_left, nums1_right=0, len(nums1) - 1
        while True:
            nums1_median = (nums1_left+nums1_right)//2
            nums2_median=half_len-nums1_median-1-1

            nums1_l=nums1[nums1_median] if nums1_median>=0 else -float('inf')
            nums1_r=nums1[nums1_median+1] if nums1_median+1<len(nums1) else float('inf')
            nums2_l=nums2[nums2_median] if nums2_median>=0 else -float('inf')
            nums2_r=nums2[nums2_median+1] if nums2_median+1<len(nums2) else float('inf')

            # even
            if(total_len%2==0):
                if(max(nums1_l, nums2_l)<=min(nums2_r, nums1_r)):
                    return (max(nums1_l, nums2_l)+min(nums2_r, nums1_r))/2

            # odd
            if(total_len%2==1):
                if(max(nums1_l, nums2_l)<=min(nums2_r, nums1_r)):
                    return min(nums2_r, nums1_r)
                
            if(nums1_l>nums2_r):
                nums1_right=nums1_median-1
            else:
                nums1_left=nums1_median+1