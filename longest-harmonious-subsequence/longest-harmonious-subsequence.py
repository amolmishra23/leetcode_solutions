class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Straight forward question. We need to find such a subsequence, only containing x, x+1. 
        And such that max occurence of numbers happen.
        Hence just find the count of numbers, and iterate to find, x and x+1 occurence, and return the same in res. 
        """
        count, res = Counter(nums), 0
        
        for x in count:
            if x+1 in count:
                res = max(res, count[x]+count[x+1])
                
        return res
        
        