class TimeMap:

    def __init__(self):
        self.name_timestap_value=defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name_timestap_value[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.name_timestap_value:
            return ""
        values=self.name_timestap_value[key]
        l=0
        r=len(values) - 1
        ans=""
        while l<=r:
            median=(l+r)//2
            if(timestamp==values[median][0]):
                ans=values[median][1]
                break
            elif(timestamp<values[median][0]):
                r=median-1
            else:
                ans = values[median][1]                
                l=median+1
                
        return ans
