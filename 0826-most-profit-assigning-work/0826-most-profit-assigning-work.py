class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        Same work can be repeated multiple times
        1 worker can take up only 1 task
        
        So we sort our difficulty, workers. And try to map the best difficulty task for the worker.
        Among them whatever is the max profit, can be done by the worker. 
        this best task can also be used in the next attempt very well. 
        """
        jobs, res = sorted(zip(difficulty, profit)), 0
        
        i, best = 0, 0
        
        for ability in sorted(worker):
            while i<len(jobs) and jobs[i][0]<=ability:
                best = max(best, jobs[i][1])
                i+=1
            res += best
            
        return res