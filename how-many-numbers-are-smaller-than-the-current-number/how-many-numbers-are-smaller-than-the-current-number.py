class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*102
        
        # storing stuff 1 index ahead
        # more like, if for 0, we store at index 1
        for num in nums: count[num+1] += 1
        
        # now for number 2, its count is at index 3
        # sum all the counts until index 2. 
        # that is the answer for number 2
        for i in range(1, 102): count[i] += count[i-1]
            
        # hence we return the same answer. 
        return [count[num] for num in nums]