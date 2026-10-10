class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        left_max_boundary=0
        right_max_boundary=0
        for i in range(len(height)):
            left_max_boundary=max(left_max_boundary, height[i])
            current_water_contain=left_max_boundary-height[i]
            left_max[i]=max(0, current_water_contain)
        for i in range(len(height)-1,-1,-1):
            right_max_boundary=max(right_max_boundary, height[i])
            current_water_contain=right_max_boundary-height[i]
            right_max[i]=max(0, current_water_contain)
        water_sum=[0]*len(height)
        for i in range(len(height)):
            water_sum[i]=min(left_max[i], right_max[i])
        return sum(water_sum)