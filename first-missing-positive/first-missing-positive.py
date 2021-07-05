class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        i, n = 0, len(arr)

        while i<n:
            j = arr[i]-1

            if 0<arr[i]<=n and arr[i]!=arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i+=1

        for i in range(n):
            if arr[i] != i+1:
                return i+1

        return n+1