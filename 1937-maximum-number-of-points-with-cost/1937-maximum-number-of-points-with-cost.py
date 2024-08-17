class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        row = points[0]
        
        for r in range(1, rows):
            next_row = points[r].copy()
            
            left, right = [0]*cols, [0]*cols
            left[0] = row[0]
            for c in range(1, cols):
                left[c] = max(left[c-1]-1, row[c])
                
            right[cols-1]= row[cols-1]
            for c in range(cols-2, -1, -1):
                right[c] = max(row[c], right[c+1]-1)
                
            for c in range(cols):
                next_row[c] += max(left[c], right[c])
            row = next_row
            
        return max(row)
        