class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        Sliding window approach
        Mark the boundaries. And everytime we find a valid subarray range, add it. 
        """
        res = 0
        start_idx, mink_idx, maxk_idx = 0, -1, -1

        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                start_idx = i+1
                mink_idx = -1
                maxk_idx = -1
            
            if nums[i]==minK: mink_idx=i
            if nums[i]==maxK: maxk_idx=i

            res += max(0, min(mink_idx, maxk_idx) - start_idx+1)

        return res