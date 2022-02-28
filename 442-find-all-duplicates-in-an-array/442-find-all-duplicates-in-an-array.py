class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        
        while i<len(arr):
            # expected index of the number
            j = arr[i]-1
            if arr[i]!=arr[j]:
                # attempting to place number at ith index, at index arr[i]-1
                arr[i], arr[j] = arr[j], arr[i]
            else:
                # this index is all good. lets proceed to next index
                i+=1
        
        res = []
        for i in range(len(arr)):
            if arr[i]!=i+1: res.append(arr[i])
                
        return res
        