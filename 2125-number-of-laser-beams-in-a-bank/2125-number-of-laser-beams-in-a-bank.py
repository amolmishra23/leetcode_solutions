class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        onesCount = list(map(lambda x: x.count("1"), bank))
        onesCount = [num for num in onesCount if num>0]
        return sum(a*b for a, b in zip(onesCount[:-1], onesCount[1:]))
        
            