class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        target, result = 0, 0
        
        for i in range(len(A)):
            """
            goal is to make all elements of array unique here
            so we sort the array and then try next elem to be bigger than target elem
            Else we need to add the diff in the result
            """
            if A[i]>=target: target=A[i]+1
            else:
                result += target-A[i]
                target+=1
        
        return result