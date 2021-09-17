class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, res = Counter(nums1), []
        
        for x in nums2:
            if count1[x]>0:
                res.append(x)
                count1[x]-=1
                
        return res