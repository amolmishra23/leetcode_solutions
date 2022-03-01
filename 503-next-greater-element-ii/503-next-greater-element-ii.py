class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def ngr(arr):
            res = [None]*len(arr)
            stk = []
            
            for i in range(len(arr)-1, -1, -1):
                while stk and stk[-1] <= arr[i]: stk.pop()
                res[i] = -1 if not stk else stk[-1]
                stk.append(arr[i])
                
            return res
        
        return ngr(nums+nums)[:len(nums)]
            