class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        topsCounter, bottomCounter = Counter(tops), Counter(bottoms)
        res = float("inf")

        topEl, topCount = topsCounter.most_common(1)[0]
        bottomEl, bottomCount = bottomCounter.most_common(1)[0]

        def solve(el, arr1, arr2):
            res=0
            for a,b in zip(arr1, arr2):
                if a==el:
                    continue
                elif b==el:
                    res+=1
                else:
                    res=float("inf")
                    break
            
            return res
        
        res = min(solve(topEl, tops, bottoms), solve(bottomEl, bottoms, tops))
        return -1 if res==float("inf") else res