class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        l, r, score, res = 0, len(tokens)-1, 0, 0
        
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                score+=1
                l+=1
                res = max(res, score)
            elif score:
                score-=1
                power+=tokens[r]
                r-=1
            else:
                break
            
        return res