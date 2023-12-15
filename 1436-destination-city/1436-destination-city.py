class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dst = list(map(set, zip(*paths)))
        return dst.difference(src).pop()