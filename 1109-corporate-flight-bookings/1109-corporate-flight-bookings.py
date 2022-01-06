class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Question is an easy one, but written in a shitty way. 
        flight = 5
        [2,5,25] means from flight 2 until flight 5 we have 25 seats. includes for flight 2,3,4,5
        Solving using prefix sum array concept
        """
        res = [0]*(n+1)
        
        for start,end,seats in bookings:
            res[start-1] += seats
            res[end] -= seats
            
        for i in range(1, n+1):
            res[i] += res[i-1]
            
        res.pop()
        return res