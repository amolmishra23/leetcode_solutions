class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def bit_count(bits):
            count = 0
            while bits:
                bits &= bits-1
                count +=1
            return count
        return ['{}:{:02d}'.format(h, m) for h in range(12) for m in range(60) if bit_count(h)+bit_count(m)==num]