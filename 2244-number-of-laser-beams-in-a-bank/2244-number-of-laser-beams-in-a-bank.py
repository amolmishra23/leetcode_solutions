class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        onesCount = [num for num in list(map(lambda x: x.count("1"), bank)) if num>0]
        return sum(a*b for a, b in zip(onesCount[:-1], onesCount[1:]))
        