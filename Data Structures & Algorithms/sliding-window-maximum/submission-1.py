class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initia the window
        l=0
        r=k
        ans=[]
        ans.append(max(nums[l:k]))
        for r in range(k, len(nums)):
            l=r-k+1
            print(f"r: {r} l: {l}")
            ans.append(max(nums[l:r+1]))
        return ans