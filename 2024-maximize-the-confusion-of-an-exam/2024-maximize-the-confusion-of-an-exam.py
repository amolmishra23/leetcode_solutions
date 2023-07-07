class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count, res = Counter(), 0
        i=0
        
        for j in range(len(answerKey)):
            count[answerKey[j]] += 1
            
            if count["T"]>k and count["F"]>k:
                count[answerKey[i]] -= 1
                i += 1
            else:
                res = max(res, j-i+1)
                
        return res
        