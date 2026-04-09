class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr=0
        right_ptr=len(numbers)-1
        ans=[]
        while(left_ptr<right_ptr):
            match_target=numbers[right_ptr]+numbers[left_ptr]  
            if(match_target>target):
                right_ptr-=1
            elif(match_target<target):
                left_ptr+=1
            else:
                ans=[left_ptr+1, right_ptr+1]
                left_ptr+=1
                return ans
        return ans 