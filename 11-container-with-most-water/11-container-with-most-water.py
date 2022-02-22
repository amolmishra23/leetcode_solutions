class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        2 pointer approach, we just keep calculating whats the max area possible
        """
        i, j = 0, len(height)-1
        
        max_area = float('-inf')
        
        while i<j:    
            curr_area = (j-i)*min(height[i], height[j])
            max_area = max(max_area, curr_area)
            if height[i]<height[j]: i+=1
            else: j-=1
                
        return max_area