class Solution:
    def reverseVowels(self, in_s: str) -> str:
        s = list(in_s)
        vs = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels = deque()
        
        for i in range(len(s)):
            if s[i] in vs: vowels.append(s[i]); s[i]="_"
        
        for i in range(len(s)):
            if s[i]=="_": s[i] = vowels.pop()
        
        return ''.join(s)