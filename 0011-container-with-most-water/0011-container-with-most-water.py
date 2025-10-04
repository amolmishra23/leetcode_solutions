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
            # at every index we find the curr area.
            # width is distance of the 2 pointers
            # height is minimum of the 2 given heights
            curr_area = (j-i)*min(height[i], height[j])
            
            # updating the max area
            max_area = max(max_area, curr_area)
            if height[i]<height[j]: i+=1
            else: j-=1
                
        return max_area