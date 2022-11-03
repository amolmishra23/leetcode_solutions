class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res, odd_exists = 0, False
        
        for word, word_count in count.items():
            if word[0]==word[1]:
                if word_count%2==0: res+=(word_count)
                else:
                    res += (word_count-1)
                    odd_exists = True
            else:
                res += min(word_count, count[word[::-1]])
            
        if odd_exists: res+=1
        return res*2
            