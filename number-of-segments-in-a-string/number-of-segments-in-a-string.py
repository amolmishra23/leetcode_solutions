class Solution:
    def countSegments(self, s: str) -> int:
        # return len(s.strip().split(" ")) if len(s.strip())>=1 else 0
        return len(s.split())