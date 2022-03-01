class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_ = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score_)+1)]
        score_to_medals = dict(zip(score_, medals))
        return [score_to_medals[x] for x in score]