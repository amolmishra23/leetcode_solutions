class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Best explanation at: https://www.youtube.com/watch?v=wRubz1zhVqk
        Logic is, at each dfs branch we keep counting how many elements are down there.
        if we have the element, we keep adding to counter. 
        """
        curr, i = 1, 1
        
        def count(curr):
            res, nei = 0, curr+1
            
            while curr <= n:
                res += min(nei, n+1) - curr
                curr *= 10
                nei *= 10
                
            return res
        
            
        while i<k:
            steps = count(curr)
            if i + steps <= k:
                curr = curr + 1
                i += steps 
            else:
                curr *= 10
                i += 1
            
        return curr