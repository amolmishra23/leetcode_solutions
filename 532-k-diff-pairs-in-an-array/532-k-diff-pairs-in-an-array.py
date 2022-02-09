class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, res = Counter(nums), 0
        
        # So as to not go over the number in repeat, we do it via map. 
        # if k>0, just take its 1 occurence, as we only check for x+k
        for x in count:
            if (k>0 and x+k in count) or (k==0 and count[x]>1): res += 1
        
        return res