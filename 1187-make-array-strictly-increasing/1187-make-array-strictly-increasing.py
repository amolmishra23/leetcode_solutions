import bisect, functools
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        
        def getSlightlyStrightlyBigger(n):
            index = bisect.bisect_right(arr2, n)
            if index == len(arr2):
                return None
            return arr2[index]
        
        @functools.lru_cache(None)
        def attempt(index, must_strictly_bigger_than):
            # If we reached the end, it is a success
            if index == len(arr1):
                return 0
            
            # Its already big enough. Dont need to replace
            if arr1[index] > must_strictly_bigger_than:
                res1 = attempt(index + 1, arr1[index])
            else:
                res1 = float('inf')
                
            # Lets replace it simply, with bigger element. (Trying all permutations)
            bigger = getSlightlyStrightlyBigger(must_strictly_bigger_than)
            if bigger is None:
                res2 = float('inf')
            else:
                res2 = attempt(index + 1, bigger)
            
            # returning whichever workflow returned us minimum steps overall. 
            return min(res1, res2 + 1)
                
        # initially we just need to be bigger than float("-inf")
        res = attempt(0, float('-inf'))
        return res if res != float('inf') else -1