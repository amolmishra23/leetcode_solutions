from bisect import bisect_left
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        max_so_far = float('-inf')
        for x in houses:
            idx = bisect_left(heaters, x)
            if 0<idx<len(heaters):
                dist = min(x-heaters[idx-1], heaters[idx]-x)
            else:
                dist = heaters[0]-x if idx == 0 else x - heaters[-1]
            max_so_far = max(dist, max_so_far)
        return max_so_far