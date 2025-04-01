class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def backtrack(i):
            if i >= len(questions): return 0
            points, brain = questions[i]
            return max(backtrack(i+1), points+backtrack(i+1+brain))
        return backtrack(0)