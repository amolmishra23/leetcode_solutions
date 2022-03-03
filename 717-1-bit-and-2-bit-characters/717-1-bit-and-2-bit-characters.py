class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        Effectively, you are looking for pairs of [1,0], pairs of [1,1], or a single [0] in the array.
[0,1] is impossible as the single [0] gets skipped.
If you do get a [1,0] or a [1,1] pair, set a flag denoting the pairing. Otherwise, falsify this flag.
If, at the end, you wind up with the pairing flag, then the result is false.
        """
        n = len(bits)
        is_one_bit=False
        i=0
        while i<n:
            if bits[i]==1:
                i+=2
                is_one_bit=False
            else:
                i+=1
                is_one_bit=True
        return is_one_bit