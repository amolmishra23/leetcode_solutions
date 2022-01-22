class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        """
        Instead of doing it the DP way exploring all possible paths
        We pick up possibilites in such a way, reducing max for opponent. Apart choosing best one for ourselves too. 
        To find that, find sum of scores in descending order, and accordingly make the choice. 
        """
        t = list(zip(A, B))
        t.sort(key = lambda x: sum(x), reverse=True)
        a_score, b_score = sum([i[0] for i in t[::2]]), sum([i[1] for i in t[1::2]])
        
        if a_score>b_score: return 1
        elif a_score<b_score: return -1
        else: return 0
        