class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed=[]
        for i in range(len(position)):
            position_speed.append((target-position[i], speed[i]))
        position_speed.sort()
        position_speed=deque(position_speed)
        print(position_speed)
        ans_stack=[]
        while(position_speed):
            if(not ans_stack):
                ans_stack.append(position_speed[0][0]/position_speed[0][1])
            else:
                if(position_speed[0][0]/position_speed[0][1]>ans_stack[-1]):
                    ans_stack.append(position_speed[0][0]/position_speed[0][1])
            if(position_speed):
                position_speed.popleft()
        print(ans_stack)
        return len(ans_stack)