class Solution:
    def nearest_smallest_left(self, arr):
        n = len(arr)
        res = [None]*n
        stk = []
        
        for i, num in enumerate(arr):
            if not stk: res[i] = -1
            elif arr[stk[-1]]<arr[i]: res[i]=stk[-1]
            else:
                while stk and arr[stk[-1]]>=arr[i]: stk.pop()
                res[i] = -1 if not stk else stk[-1]
            stk.append(i)
        
        return res
    
    def nearest_smallest_right(self, arr):
        n = len(arr)
        res = [None]*n
        stk = []
        
        for i in range(n-1, -1, -1):
            if not stk: res[i]=n
            elif arr[stk[-1]]<arr[i]: res[i] = stk[-1]
            else:
                while stk and arr[stk[-1]]>=arr[i]: stk.pop()
                res[i]=n if not stk else stk[-1]
            stk.append(i)
        
        return res
        
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==0: return 0
        if len(heights)==1: return heights[0]
        
        left = self.nearest_smallest_left(heights)
        right = self.nearest_smallest_right(heights) 
        widths = []
        
        # widths give us an idea, how wide can we spread the thing? 
        for l,r in zip(left, right):
            widths.append(r-l-1)
        max_area = 0
        
        # height is anyways given in question. So now we can find the area of rectangle.
        for h, w in zip(heights, widths):
            max_area = max(max_area, h*w)
            
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]): return 0
        m, n = len(matrix), len(matrix[0])
        
        heights = [0]*n
        max_area = 0
        
        # finding heights in the prefix sum way
        # and this will inturn be used to find the largest rectangle area. 
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j]+1 if matrix[i][j]=="1" else 0
            print (heights)
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
            
        