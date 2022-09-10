class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sum, count = [], Counter()
        
        for row in wall:
            prev, curr_row_prefix = 0, []
            for x in row[:-1]: 
                prev += x
                curr_row_prefix.append(prev)
            count.update(curr_row_prefix)
            prefix_sum.append(curr_row_prefix)
            
        return len(wall) - (max(count.values()) if count.values() else 0)
        
        