import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = collections.Counter(words)
        num_words = len(words)
        word_len = len(words[0])
        matched = 0
        res = []
        
        for i in range((len(s) - (num_words*word_len))+1):
            seen = collections.Counter()
            for j in range(num_words):
                word_index = i+j*word_len
                curr_word = s[word_index:word_index+word_len]
                if curr_word not in count: break
                    
                seen[curr_word]+= 1
                if seen[curr_word]>count[curr_word]: break
                
                if j+1 == num_words: res.append(i)
        
        return res
                    
                    
                
        