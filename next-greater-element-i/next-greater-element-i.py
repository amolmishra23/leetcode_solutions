class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def ngr(arr):
            n = len(arr)
            stk = []
            res = [None]*n
            
            for i in range(n-1, -1, -1):
                if not stk: res[i]=-1
                elif stk[-1]>arr[i]: res[i]=stk[-1]
                else:
                    while stk and stk[-1]<arr[i]: stk.pop()
                    res[i] = -1 if not stk else stk[-1]
                stk.append(arr[i])

            return res
        
        
        computed = ngr(nums2)
        res = [None]*len(nums1)
        
        for i, num in enumerate(nums1):
            res[i] = computed[nums2.index(num)]
        
        return res

                    