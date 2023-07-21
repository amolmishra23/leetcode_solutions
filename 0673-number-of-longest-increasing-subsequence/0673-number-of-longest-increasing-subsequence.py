class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        self.len, self.count = [1]*n, [1]*n
        self.max = float("-inf")
        
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if self.len[j]+1>self.len[i]:
                        self.len[i] = self.len[j]+1
                        self.count[i] = self.count[j]
                    elif self.len[j]+1==self.len[i]:
                        self.count[i] += self.count[j]
            self.max = max(self.max, self.len[i])
            
        res = 0
        for i in range(n):
            if self.len[i]==self.max: res += self.count[i]
                
        return res
                
                        