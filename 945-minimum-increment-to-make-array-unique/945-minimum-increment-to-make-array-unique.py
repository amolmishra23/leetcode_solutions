class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        target, result = 0, 0
        
        for i in range(len(A)):
            if A[i]>=target: target=A[i]+1
            else:
                result += target-A[i]
                target+=1
        
        return result