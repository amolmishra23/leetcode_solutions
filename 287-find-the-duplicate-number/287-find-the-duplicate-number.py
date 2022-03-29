class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        i = 0

        while i<len(arr):
            j = arr[i]-1
            if arr[i]!=arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i+=1

        for i in range(len(arr)):
            if arr[i]!=i+1:
                return arr[i]

        return -1