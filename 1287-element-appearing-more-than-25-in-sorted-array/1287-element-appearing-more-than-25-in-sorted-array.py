class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k = int(len(arr)*0.25)
        return [x for x in arr[::k] if (bisect.bisect(arr, x) - bisect.bisect_left(arr, x)) > k][0] if k else arr[0]