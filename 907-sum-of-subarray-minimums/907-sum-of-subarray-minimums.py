class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Detailed understanding: https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
        """
        n, mod = len(arr), 10**9+7
        
        left, right, s1, s2 = [None]*n, [None]*n, [], []
        
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > arr[i]: count += s1.pop()[1]
            left[i] = count
            s1.append((arr[i], count))
            
        for i in range(n-1, -1, -1):
            count = 1
            while s2 and s2[-1][0] >= arr[i]: count += s2.pop()[1]
            right[i] = count
            s2.append((arr[i], count))
            
        return sum(a*l*r for a,l,r in zip(arr,left,right))%mod