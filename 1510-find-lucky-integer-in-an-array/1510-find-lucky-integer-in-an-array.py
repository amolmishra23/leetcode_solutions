class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count, res = Counter(arr), -1
        for k,v in count.items():
            if k==v: res=max(res, k)
        return res