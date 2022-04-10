class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def ngr(arr):
            n = len(arr)
            res = [None]*n
            stk = []
            
            for i in range(n-1, -1, -1):
                while stk and arr[stk[-1]]<arr[i]: stk.pop()
                res[i] = stk[-1] if stk else -1
                stk.append(i)
                
            return res
        
        ng = ngr(nums2)
        res = [None]*len(nums1)
        
        for i, num in enumerate(nums1):
            idx = ng[nums2.index(num)]
            res[i] = nums2[idx] if idx!=-1 else -1
            
        return res