class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        for word in sorted(d, key=lambda x:(-len(x), x)):
            i = 0
            for c in s:
                if i<len(word) and word[i]==c:
                    i+=1
            if i==len(word): return word
            
        return ""