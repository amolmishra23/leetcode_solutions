class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        # Maintaining two stacks
        # 1) left parenthesis's indexes
        # 2) star's ("*") indexes
        left = list()
        star = list()
        
        for i, c in enumerate(s):
            if c == "*":
                star.append(i)
            elif c == "(":
                left.append(i)
            elif c == ")":
                # When encounter "*"
                # Prefer balance out using the left "(" than "*"
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        if len(left) > len(star):
            # Checking the counts of residual left and star
            return False
        
        while left and star:
            # Compare the indexes of left and star
            # Make sure star came aftewards, if not, return False
            if left.pop() > star.pop():
                return False
        
        return True
        
