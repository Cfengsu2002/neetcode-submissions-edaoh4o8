class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array=(n+1)*[0]
        print(dp_array)
        dp_array[-1]=1
        dp_array[-2]=2
        if(n<=2):
            return dp_array[-n]
        for i in range(len(dp_array)-3,-1,-1):
            dp_array[i]=dp_array[i+1]+dp_array[i+2]
        return dp_array[1]
