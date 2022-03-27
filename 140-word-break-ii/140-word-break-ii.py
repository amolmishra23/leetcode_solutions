class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]     