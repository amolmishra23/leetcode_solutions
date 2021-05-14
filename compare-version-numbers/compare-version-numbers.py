class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        
        for x in range(max(len(v1), len(v2))):
            version1 = v1[x] if x<len(v1) else 0
            version2 = v2[x] if x<len(v2) else 0
            
            if version1 > version2: return 1
            elif version2 > version1: return -1
        
        return 0