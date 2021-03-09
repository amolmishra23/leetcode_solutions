class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(nums, n):
            for i in range(n):
                if abs(nums[i]-nums[n])==n-i or nums[i]==nums[n]: return False
            return True
        
        def solve(nums, index, path, res):
            if index==len(nums):
                res.append(path)
                return
            
            for i in range(len(nums)):
                nums[index] = i
                if is_valid(nums, index):
                    tmp = "."*len(nums)
                    solve(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)
                    
        res = []
        solve([-1]*n, 0, [], res)
        return len(res)