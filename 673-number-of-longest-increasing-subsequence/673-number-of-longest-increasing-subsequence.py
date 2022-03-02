class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        LIS means the numbers have to be strictly increasing. 
        First we try to find which is LIS. Being part of which sequence is most helpful through DP.
        We also keep updating the count, if we found more than 1 sequence with the same max_len
        in the end we just return the no of sequences with the max len. 
        """
        n = len(nums)
        len_, count_ = [1]*(n), [1]*(n)
        max_=float('-inf')
        
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if len_[j]+1>len_[i]:
                        len_[i] = len_[j]+1
                        count_[i] = count_[j]
                    elif len_[j]+1==len_[i]:
                        count_[i]+=count_[j]
            max_=max(max_, len_[i])
                        
        res = 0
        for i in range(n):
            if len_[i]==max_: res+=count_[i]
                
        return res