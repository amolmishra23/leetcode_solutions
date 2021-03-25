class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:          
        r, c = len(matrix), len(matrix[0])
        
        low, high = 0, r*c-1
        
        while low<=high:
            mid = low + (high-low)//2
            elem = matrix[mid//c][mid%c]
            
            if elem == target: return True
            elif elem>target: high = mid-1
            else: low = mid+1
                
        return False