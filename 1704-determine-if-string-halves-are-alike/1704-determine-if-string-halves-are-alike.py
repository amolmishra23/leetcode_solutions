class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        a, b = s[:n], s[n:]
        is_vowel = lambda x: x.lower() in {"a", "e", "i", "o", "u"}
        return sum(is_vowel(ch) for ch in a) == sum(is_vowel(ch) for ch in b)
    