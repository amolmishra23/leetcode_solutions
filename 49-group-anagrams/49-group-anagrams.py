class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(x)) for x in strs]
        
        groups = {}
        
        for idx, x in enumerate(sorted_strs):
            if x in groups:
                groups[x].append(strs[idx])
            else:
                groups[x] = [strs[idx]]
                
        return groups.values()