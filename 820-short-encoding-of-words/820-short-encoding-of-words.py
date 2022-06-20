class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        Because the problem involves suffix, no brainer to apply reverse trie
        We go on adding all strings to trie
        And in the end, only include the complete words as part to our soln (not common ones from trie)
        
        O(NK), O(NK)
        """
        root = dict()
        leaves = []
        
        for word in set(words):
            curr = root
            for w in word[::-1]:
                curr[w] = curr = curr.get(w, {})
            leaves.append((curr, len(word)+1))
        
        return sum(depth for node, depth in leaves if len(node)==0)