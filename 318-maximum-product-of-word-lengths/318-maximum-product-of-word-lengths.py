class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_bitmap = [0]*len(words)
        words.sort(key = lambda x: len(x), reverse=True)
        for idx, word in enumerate(words): 
            for ch in word: 
                words_bitmap[idx] |= (1<<(ord(ch)-ord('a')))
                
        res = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i])*len(words[j]) <= res: break
                if (words_bitmap[i]&words_bitmap[j]) == 0: res = max(res, len(words[i])*len(words[j]))

        return res
        