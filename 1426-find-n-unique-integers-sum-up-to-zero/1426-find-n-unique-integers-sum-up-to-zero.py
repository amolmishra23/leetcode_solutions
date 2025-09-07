class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n//2
        if n%2==0: return list(range(-half, 0)) + list(range(1, half+1))
        else: return list(range(-half, half+1))