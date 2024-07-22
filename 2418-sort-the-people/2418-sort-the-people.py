class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [elem[0] for elem in sorted(zip(names, heights), key = lambda x: -x[1])]