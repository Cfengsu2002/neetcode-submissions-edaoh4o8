class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # map construction
        flight_itinerary_linked_list=defaultdict(list)
        for source_flight, end_flight in tickets:
            flight_itinerary_linked_list[source_flight].append(end_flight)

        # sort the list
        for key in flight_itinerary_linked_list.keys():
            flight_itinerary_linked_list[key].sort()
        print(flight_itinerary_linked_list)
        
        res = ["JFK"]
        def dfs(src):
            if (len(res)==len(tickets)+1):
                return True
            if src not in flight_itinerary_linked_list:
                return False
            temp_list=flight_itinerary_linked_list[src].copy()
            for i in range(len(temp_list)):
                val = flight_itinerary_linked_list[src].pop(i)
                res.append(val)
                if dfs(val):
                    return True
                flight_itinerary_linked_list[src].insert(i, val)
                res.pop()
            return False
        dfs('JFK')
        return res