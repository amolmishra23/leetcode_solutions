class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital, max_profit = [], []
        
        # 2 step process
        # Step 1 => Create the minheap to find the projects which we can do in our budget
        for i in range(len(capital)):
            heapq.heappush(min_capital, (capital[i], i))
            
        curr_capital = w
        
        for i in range(k):
            # Step 2 => For our budget projects add them to a max heap
            while min_capital and min_capital[0][0]<=curr_capital:
                _, idx = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -profits[idx])
            
            # if no project is possible, we can return the result
            if not max_profit: break
            
            # else we add the project which had the max profit possible. 
            curr_capital += (-heapq.heappop(max_profit))
            
        return curr_capital