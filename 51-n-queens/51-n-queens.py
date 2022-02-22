class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(nums, n):
            for i in range(n):
                """
                A very weird formula to deduce if the elements lie in the same diagonal.(both diagonal and anti-diagonal)
                Lets say we made a queen placement at (3,1). And already had a queen at (1,3). Technically its clashing at the anti-diagonal. 
                
                row indexes are 3,1
                col indexes are 1,3
                rows: 3-1=2
                cols: abs(3-1) = 2
                Hence they are attacking each other
                
                Lets discuss of diagonal. (0,1) (2,3)
                row indexes are 0,2
                col indexes are 1,3
                cols: abs(1-3)=2
                rows: 2-0=2
                Hence they are attacking each other
                
                If we have 2 points lets say (0,2), (2,2)
                Because they both lie in col "2", they can attack each other. 
                
                We never need to check if queen lie in same row. Because for each row, we just have 1 column index. 
                """
                if abs(nums[i]-nums[n])==n-i or nums[i]==nums[n]: return False
            return True
        
        def solve(nums, index, path, res):
            if index == len(nums):
                res.append(path)
                return
            
            for i in range(len(nums)):
                nums[index] = i
                if is_valid(nums, index):
                    tmp = "."*len(nums)
                    solve(nums, index+1, path + [tmp[:i]+"Q"+tmp[i+1:]], res)
        
        res = []
        """
        Every row can have 1 only queen. Hence we store the col index, at which queen is placed! [-1]*n
        For nth rol, the queen is placed at nums[n])
        """
        solve([-1]*n, 0, [], res)
        return res