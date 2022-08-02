class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        def countLessOrEqual(x):
            count = 0
            c = n-1
            for r in range(m):
                while c>=0 and matrix[r][c]>x: c-=1
                count += (c+1)
            return count
        
        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        
        while left<=right:
            mid = (left+right)//2
            if sum(bisect_right(row, mid) for row in matrix)>=k:
                ans = mid
                right = mid-1
            else:
                left = mid+1
                
        return ans