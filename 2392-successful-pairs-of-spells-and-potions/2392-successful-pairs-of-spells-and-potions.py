class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(); res = []
        for s in spells:
            q, r = divmod(success, s)
            req = q + (r!=0)
            res.append(len(potions) - bisect.bisect_left(potions, req))
        
        return res