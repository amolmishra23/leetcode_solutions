class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        """
        in every iteration, [a,b,c,d] => we are basically adding 0a+1b+2c+3d. 
        next time it will be 0d+1a+2b+2c. Basically adding sum, as sum contains 1 of all elements, and deleting last element. 
        formula deducted for the same is curr += sum - n*A[i]
        """
        if not A: return 0
        sum_ = sum(A)
        n = len(A)
        curr_max = float('-inf')
        curr = 0
        for i in range(n): curr += i*A[i]
            
        for i in range(n-1, -1, -1):
            curr += sum_ - n*A[i]
            curr_max = max(curr_max, curr)
            
        return curr_max