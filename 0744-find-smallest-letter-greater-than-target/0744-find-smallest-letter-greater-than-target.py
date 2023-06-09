class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0]>target or letters[-1]<=target: return letters[0]
        
        low, high, res = 0, len(letters)-1, ""
        
        while low<high:
            mid = (low+high)//2
            if letters[mid]<=target:
                low=mid+1
            elif letters[mid]>target:
                high=mid
                
        return letters[low]