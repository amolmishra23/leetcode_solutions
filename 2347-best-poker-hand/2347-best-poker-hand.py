class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush = lambda: "Flush" if len(set(suits))==1 else None
        tok = lambda: "Three of a Kind" if Counter(ranks).most_common(1)[0][1]>=3 else None
        pair = lambda: "Pair" if Counter(ranks).most_common(1)[0][1]>=2 else "High Card"
        return flush() or tok() or pair()