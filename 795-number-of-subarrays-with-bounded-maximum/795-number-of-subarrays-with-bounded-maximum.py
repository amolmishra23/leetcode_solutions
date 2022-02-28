class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """
        no of subsets with elem less than R(bigger limit) - no of subsets with elem less than L-1(lower limit)
        Same known concept of no of subarrays for particular length array. As long as elements come within the bound, we keep increasing our window size and keep adding it, as in the end it is n*(n+1)/2. as soon as something is out we reset our bound index. 
        """
        def num_subsets(A, bound):
            result, curr = 0, 0
            
            for i in A:
                curr = curr+1 if i<=bound else 0
                result += curr
            
            return result
        
        return num_subsets(A, R) - num_subsets(A, L-1)