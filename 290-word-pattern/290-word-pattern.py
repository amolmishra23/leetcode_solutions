class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # question is easy one, just need to see if elements are perfectly mapped 1:1
        # we mark each element, by an index, based on their 1st occurence in array/str
        # if all the indexes are same both array. we return True. Else False. 
        return [pattern.index(x) for x in pattern] == [s.split(" ").index(x) for x in s.split(" ")]