class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Solving it using O(n**2)
        n, map_,res = len(nums1), defaultdict(int), 0
        
        for i in range(n):
            for j in range(n):
                map_[nums1[i]+nums2[j]] += 1
        
        for i in range(n):
            for j in range(n):
                res += map_[-(nums3[i]+nums4[j])]
                
        return res
        