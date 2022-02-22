class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Try to read the code, with the following example: "()(()"
        """
        max_length, stk = 0, [-1]
        
        for i, chr in enumerate(s):
            if chr=='(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                if stk:
                    max_length = max(max_length, i-stk[-1])
                else:
                    stk.append(i)
        return max_length