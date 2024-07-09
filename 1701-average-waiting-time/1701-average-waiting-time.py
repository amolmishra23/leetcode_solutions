class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res, chef = 0, 0
        
        for arrival, duration in customers:
            chef = max(arrival, chef)+duration
            res += (chef-arrival)
            
        return res/len(customers)