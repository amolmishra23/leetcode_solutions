class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        
        for op in operations:
            if op == "--X": res -= 1
            elif op == "++X": res += 1
            elif op == "X--": res-=1
            elif op == "X++": res+=1
        
        return res