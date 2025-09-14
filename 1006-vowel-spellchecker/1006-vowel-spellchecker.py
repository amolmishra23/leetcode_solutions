class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word):
            res = []
            for ch in word:
                res.append("*" if ch in vowels else ch)
            return "".join(res)

        exact = set(wordlist)
        lowercase, pattern = {}, {}

        for w in wordlist:
            if w.lower() not in lowercase:
                lowercase[w.lower()] = w
            if devowel(w.lower()) not in pattern:
                pattern[devowel(w.lower())] = w

        res = []
        for q in queries:
            if q in exact: res.append(q); continue
            if q.lower() in lowercase: res.append(lowercase[q.lower()]); continue
            if devowel(q.lower()) in pattern: res.append(pattern[devowel(q.lower())]); continue
            res.append("")

        return res