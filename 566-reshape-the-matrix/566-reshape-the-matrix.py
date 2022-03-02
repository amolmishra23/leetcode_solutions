class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        if m==0: return nums
        n = len(nums[0])
        
        
        if m*n != r*c: return nums
        else:
            res = [[None]*c for _ in range(r)]
            flat_list = sum(nums, [])
            k = 0
            for i in range(r):
                for j in range(c):
                    res[i][j] = flat_list[k]
                    k+=1
                    
            return res