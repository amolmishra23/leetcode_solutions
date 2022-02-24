class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x), reverse=True)
        bits = [0]*len(words)
        
        for i in range(n):
            for c in words[i]:
                bits[i] |= (1 << (ord(c) - ord('a')))
        
        max_product = 0
        for i in range(n):
            if len(words[i])**2 <= max_product: break
            
            for j in range(i+1, n):
                if len(words[i]*len(words[j])) <= max_product: break
                if not (bits[i] & bits[j]): max_product = len(words[i])*len(words[j])
        
        return max_product