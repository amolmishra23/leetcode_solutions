class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c:i for i, c in enumerate(s)}
        stack = ["!"]
        visited = set()
        
        for i, symbol in enumerate(s):
            # one of the lower lexicographical character that we already visited
            if symbol in visited: continue
            
            # remove all such elements which have occured sometime later and 
            # are lexicographically smaller
            while symbol<stack[-1] and last_occ[stack[-1]]>i: visited.remove(stack.pop())
                
            # add this element to stack 
            stack.append(symbol)
            
            # add this element to the visited set
            visited.add(symbol)
            
        return "".join(stack)[1:]