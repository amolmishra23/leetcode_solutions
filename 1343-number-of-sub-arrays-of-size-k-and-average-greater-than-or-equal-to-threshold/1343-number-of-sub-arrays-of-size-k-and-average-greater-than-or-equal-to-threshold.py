class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        res, curr = 0, sum(arr[0:k])
        res += 1 if curr>=threshold*k else 0
        
        for i in range(k, n):
            curr += arr[i]-arr[i-k]
            res += (curr>=threshold*k)
        
        return res