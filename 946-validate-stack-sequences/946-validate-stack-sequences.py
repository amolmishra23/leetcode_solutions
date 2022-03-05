class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        s=[]
        
        for v in pushed:
            s.append(v)
            while s and i<len(pushed) and popped[i]==s[-1]:
                s.pop()
                i+=1
        
        return not s