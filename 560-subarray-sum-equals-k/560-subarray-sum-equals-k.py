class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0]=1
        res, su = 0, 0
        
        for x in nums:
            su += x
            # how many times previously has same sum occured. based on that we can add to res
            res += count[su-k]
            # simple logic, if in prefix sum we get 1,2,0,2,5
            # There are 2 subarrays using which we can get sum of 3.
            # 2,0,2,5 and 2,5. Because we just care about 5-2=3 diff should come. 
            count[su] += 1
            
        return res