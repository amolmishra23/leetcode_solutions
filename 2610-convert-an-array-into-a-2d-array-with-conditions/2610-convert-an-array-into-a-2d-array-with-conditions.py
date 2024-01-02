class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = [[] for _ in range(max(count.values()))]
        
        for el, c in count.items():
            for i in range(c):
                res[i].append(el)
                
        return res