class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs, res = ["".join(sorted(x)) for x in strs], defaultdict(list)
        
        for i, s in enumerate(sorted_strs): res[s].append(strs[i])
            
        return res.values()