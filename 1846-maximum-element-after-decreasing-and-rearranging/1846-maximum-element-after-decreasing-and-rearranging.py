class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)):
            arr[i] = min(arr[i], arr[i-1]+1 if i>0 else 1)            
        return arr[-1]