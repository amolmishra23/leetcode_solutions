class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        Need to check if the current 1 has occured atleast after k indexes. 
        If yes, we update the most_recent index.
        If no, we return false. 
        """
        most_recent = -1
        
        for i, n in enumerate(nums):
            if n==1:
                if most_recent==-1 or i-most_recent-1>=k:
                    most_recent=i
                else:
                    return False
        
        return True