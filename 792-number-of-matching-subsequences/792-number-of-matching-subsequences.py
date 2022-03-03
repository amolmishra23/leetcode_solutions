import collections

class Solution:
#     def numMatchingSubseq(self, S: str, words: List[str]) -> int:
#         waiting = collections.defaultdict(list)
#         for word in words:
#             it = iter(word)
#             waiting[next(it, None)].append(it)
        
#         for chr in S:
#             for it in waiting.pop(chr, ()):
#                 waiting[next(it, None)].append(it)
                
#         return len(waiting[None])
    """
    Basic concept lies around, if our string is abcde, make a dict like this
    {
        "a": [0],
        "b": [1],
        "c": [2],
        "d": [3],
        "e": [4]
    }
    
    Now in case we want to check for a subsequence ace, 
    check if 
    -> -1 can be inserted in [0], such that, its not inserted at the last location of list. 
    -> 0 can be inserted in [2], such that, its not inserted at the last location of list [2]
    -> 2 can be inserted in [4], such that, its not inserted at the last location of list[4]
    
    If thats possible, we are a valid subsequence. If thats not, we arent a valid subsequence. 
    
    like if our input is bb, 
    -> -1 can be inserted in [0]
    -> 0 can be inserted in [0] such that its not at last location of the list.means we are out of bounds and its not a valid subsequence. 
    
    """
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def is_sub_seq(word):
            pre_pos = -1
            
            for c in word:
                if c not in index_map: return False
                
                index = bisect_right(index_map[c], pre_pos)
                
                if index == len(index_map[c]):
                    return False
                
                pre_pos = index_map[c][index]
                
            return True
                
                
        index_map = collections.defaultdict(list)
        for i, c in enumerate(S):
            index_map[c].append(i)
            
        ans = 0
        
        for word in words:
            if is_sub_seq(word): ans+=1
        
        return ans