class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2,nums1)
        
        cnt = Counter(nums1)
        res = []
        for x in nums2:
            if cnt[x]>0:
                cnt[x]-=1
                res.append(x)
                
        return res