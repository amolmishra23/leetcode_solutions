class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        query_to_idx = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [None]*len(queries)
        
        res, j = 0, 0
        for q, i in query_to_idx:
            while j<len(items) and items[j][0]<=q:
                res = max(res, items[j][1])
                j+=1
            ans[i] = res
            
        return ans