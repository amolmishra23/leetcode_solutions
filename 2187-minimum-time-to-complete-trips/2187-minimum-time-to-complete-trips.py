class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        number_of_trips = lambda time_elapsed: sum(time_elapsed//tm for tm in time)
        low, high = 1, min(time)*totalTrips
        
        while low<high:
            mid = low + (high-low)//2
            completed_trips = number_of_trips(mid)
            
            if completed_trips>=totalTrips: high = mid
            elif completed_trips<totalTrips: low=mid+1
                
        return low