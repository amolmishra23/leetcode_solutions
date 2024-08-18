class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 0
        
        for j in range(1, len(arr)):
            if arr[j]!=arr[j-1]: 
                i += 1
                arr[i] = arr[j]
            
        return i+1