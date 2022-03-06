class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Playing around with indexes in order to do a manual zip sort of operation on 1st and 2nd half of the array
        """
        
        res = [None]*len(nums)
        i, j, idx = 0, n, 0
        while i<n:
            res[idx] = nums[i]
            res[idx+1] = nums[j]
            i+=1
            j+=1
            idx+=2
        return res
            