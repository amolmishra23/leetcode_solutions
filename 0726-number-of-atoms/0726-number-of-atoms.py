import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        
        # in the final formula, whatever atoms, we need to keep count of it
        stack = [collections.Counter()]
        i=0
        
        while i<n:
            # if new bracket starts, its new molecule, so we add a new counter
            if formula[i]=="(":
                stack.append(collections.Counter())
                i += 1
            # if the bracket ended here, we need to just find the integer and multiply to every element in curr counter
            elif formula[i]==")":
                top = stack.pop()
                i += 1
                i_start = i
                while i<n and formula[i].isdigit(): i+=1
                mul = int(formula[i_start:i] or 1)
                # for the last atom, we just multiply it by whatever specified
                for name, v in top.items():
                    stack[-1][name] += mul*v
            else:
                # find the molecule
                # First capital letter, followed by small letters
                i_start = i
                i+=1
                while i<n and formula[i].islower(): i+=1
                name = formula[i_start:i]
                i_start = i
                # Find digits for the current atom, as multiplicity
                while i<n and formula[i].isdigit(): i+=1
                multiplicity = int(formula[i_start:i] or 1)
                # Store the atom and its multiplicity
                stack[-1][name] += multiplicity
        
        res = ""
        
        for name in sorted(stack[-1]):
            num = ""
            if stack[-1][name]>1: 
                num=str(stack[-1][name])
            res += name+num
            
        return res