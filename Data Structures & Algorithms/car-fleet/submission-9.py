class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_speed_arrive_time=[]
        for i in range(len(position)):
            arrive_time=(target-position[i])/speed[i]
            time_speed_arrive_time.append([position[i], speed[i], arrive_time])
        time_speed_arrive_time.sort()
        car_fleet=len(position)
        while len(time_speed_arrive_time)!=1:
            behind_position, behind_speed, behind_arrive_time=time_speed_arrive_time.pop()
            if(behind_arrive_time>=time_speed_arrive_time[-1][-1]):
                car_fleet-=1
                time_speed_arrive_time[-1][-1]=behind_arrive_time
        return car_fleet