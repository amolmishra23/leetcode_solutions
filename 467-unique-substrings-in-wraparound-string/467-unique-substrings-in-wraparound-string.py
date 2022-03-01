class Solution:
    """
    Each single charecter contribution is initialized to 1
    if the order is continued, the contribution is increased by 1 from previous character contribution
    example string zabce
    Values got incremented in the following way

    z -> 1
    a -> 1 + 1 (or) z + 1 -> 2
    b -> 1 + 1 + 1 (or) a + 1 -> 3
    c -> 1 + 1 + 1 + 1 (or) b + 1 -> 4
    e -> 1 (ord(j) - ord(i)) % 26 != 1 here
    So the final answer is contribution from z + a + b + c + e (1 + 2 + 3 + 4 + 1 = 11)

    max(res[j], l) is required to handle cases where the character is repeated.
    For example in zaba, since each each unique character is assigned as key to res, the 2nd a contribution should not replace the 1st a contribution until it exceeds the 1st a contribution
    """
    def findSubstringInWraproundString(self, p):
        res = {i: 1 for i in p}
        print (res)
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())