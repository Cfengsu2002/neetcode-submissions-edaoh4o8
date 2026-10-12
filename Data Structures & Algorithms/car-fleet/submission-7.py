class Solution:
    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        cars = []

        for i in range(len(position)):
            arrive_time = (target - position[i]) / speed[i]
            cars.append([position[i], arrive_time])
        cars.sort(reverse=True)
        car_fleet = 0
        fleet_time = 0
        for pos, arrive_time in cars:
            if arrive_time > fleet_time:
                car_fleet += 1
                fleet_time = arrive_time
        return car_fleet