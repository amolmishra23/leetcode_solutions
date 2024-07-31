class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """
        This problem is very much like the coin change problem
        
        """
        @lru_cache(None)
        def solve(i):
            if i == len(books): return 0
            curr_width = shelf_width
            max_height = 0
            res = float("inf")
            
            for j in range(i, len(books)):
                width, height = books[j]
                if width>curr_width: break
                curr_width -= width
                max_height = max(max_height, height)
                res = min(res, max_height + solve(j+1))
            return res
        
        return solve(0)