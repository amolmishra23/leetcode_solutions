class Solution:
    def sortVowels(self, s):
        VOWELS="AEIOUaeiou"
        only_vowels = sorted([ch for ch in s if ch in VOWELS], reverse=True)
        return "".join([only_vowels.pop() if ch in VOWELS else ch for ch in s])
        
    def sortVowelsLong(self, s: str) -> str:
        VOWELS, count ="AEIOUaeiou", Counter()
        s = list(s)
        
        for ch in s:
            if ch in VOWELS: count[ch]+=1
        
        def get_next_vowel():
            idx = 0
            while idx<len(VOWELS):
                if count[VOWELS[idx]]>0:
                    count[VOWELS[idx]]-=1; yield VOWELS[idx]
                else:
                    idx += 1
            yield ""
        
        next_vowel = get_next_vowel()
        for i in range(len(s)):
            if s[i] in VOWELS: s[i] = next(next_vowel)

        return "".join(s)