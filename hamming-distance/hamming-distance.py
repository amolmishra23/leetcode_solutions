class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1
        return count
