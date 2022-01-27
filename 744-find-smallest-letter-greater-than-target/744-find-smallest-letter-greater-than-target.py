class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # checking for the base condition
        if letters[0]>target or letters[-1]<=target:
            return letters[0]
        low, high, res = 0, len(letters)-1, ""

        while low <=high: 
            # same doing it as our pattern
            mid = (high + low) // 2
            if letters[mid]<=target:
                low = mid + 1
            elif letters[mid] > target:
                # this is potential candidate, so store it in res. 
                res = letters[mid]
                high = mid - 1

        return res