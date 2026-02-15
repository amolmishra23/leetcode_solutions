class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = [], 0
        i, j = len(a)-1, len(b)-1

        while i>=0 or j>=0 or carry:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0

            total = digit_a + digit_b + carry

            res.append(str(total%2))
            carry = total//2

            i-=1; j-=1

        return "".join(reversed(res))