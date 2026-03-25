class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        
        def can_cut(sums):
            total = sum(sums)
            current_sum = 0
            for i in range(len(sums) - 1): 
                current_sum += sums[i]
                if current_sum == total - current_sum:
                    return True
            return False
        
        return can_cut(row_sums) or can_cut(col_sums)