class Solution:
    def getReverse(self, nums):
        return [int(str(num)[::-1]) for num in nums]
        
    def countNicePairsBruteForce(self, nums: List[int]) -> int:
        revNums = self.getReverse(nums)        
        
        count = Counter()
        for n in nums:
            for r in revNums:
                count[n+r]+=1

        return sum([count//2 for key, count in count.items() if count >= 2])
        
    def countNicePairs(self, nums: List[int]) -> int:
        """
        A[i] + rev(A[j]) == A[j] + rev(A[i])
        A[i] - rev(A[i]) == A[j] - rev(A[j])
        B[i] = A[i] - rev(A[i])

        Then it becomes an easy question that,
        how many pairs in B with B[i] == B[j]
        """
        res = 0 
        count = Counter()
        
        for num in nums:
            revNum = int(str(num)[::-1])
            res += count[num-revNum]
            count[num-revNum]+=1
            
        return res % (10**9 + 7)