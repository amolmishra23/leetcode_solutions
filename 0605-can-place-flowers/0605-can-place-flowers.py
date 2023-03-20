class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        i = 0
        
        while i<len(arr) and n:
            if arr[i]==1:
                i += 2
            elif (i+1 <= len(arr)-1 and arr[i+1]==1):
                i += 3
            else:
                arr[i]=1
                i += 2
                n -= 1
                
        return n==0