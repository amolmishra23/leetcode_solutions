class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for path in paths:
            root, *files = path.split()
            for file in files:
                before,after = file.split("(")
                res[after].append(root+"/"+before)
                
        return [r for r in res.values() if len(r)>1]
            

            