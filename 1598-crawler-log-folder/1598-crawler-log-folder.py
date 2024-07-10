class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        
        for elem in logs:
            if elem == "../":
                if stk: stk.pop()
            elif elem == "./": 
                continue
            else:
                stk.append(elem)
        
        
        return len(stk)