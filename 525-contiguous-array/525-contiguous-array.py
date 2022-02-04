class Solution:
    """
    What if we have a sequence [0, 0, 0, 0, 1, 1]? the maximum length is 4, the count starting from 0, will equal -1, -2, -3, -4, -3, -2, and won't go back to 0 again. But wait, the longest subarray with equal number of 0 and 1 started and ended when count equals -2. We can plot the changes of count on a graph, as shown below. Point (0,0) indicates the initial value of count is 0, so we count the sequence starting from index 1. The longest subarray is from index 2 to 6. Which can be identified because curr counter is at -2. 
    """
    def findMaxLength(self, nums: List[int]) -> int:
        # we initialize 0 to -1, to get the subarray length properly.
        # from index 2 to beginning of array, we have a length of 3. 
        count, curr={0: -1}, 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i]==0: curr-=1
            else: curr+=1
            
            if curr in count:
                res = max(res, i-count[curr])
            else:
                # storing previously occured index for curr sum.
                # to solve it in prefix sum fashion. 
                count[curr] = i
        
        return res
            