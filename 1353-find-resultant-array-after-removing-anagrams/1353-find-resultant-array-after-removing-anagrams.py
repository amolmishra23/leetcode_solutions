class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        is_anagram = lambda w1, w2: sorted(w1)==sorted(w2)

        if not words: return []
        result = [words[0]]

        for i in range(1, len(words)):
            curr, prev = words[i], words[i-1]
            if not is_anagram(curr, prev):
                result.append(curr)

        return result