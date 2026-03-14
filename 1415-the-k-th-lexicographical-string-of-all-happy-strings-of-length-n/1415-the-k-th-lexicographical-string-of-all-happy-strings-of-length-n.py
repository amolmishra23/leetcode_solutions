class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        totalHappyStrings = 3 * (2**(n-1))

        res, choices = [], "abc"
        left, right = 1, totalHappyStrings

        for i in range(n):
            curr = left
            partition_size = (right-left+1) // len(choices)

            for c in choices:
                if k in range(curr, curr+partition_size):
                    res.append(c)
                    left, right = curr, curr+partition_size-1
                    choices = "abc".replace(c, "")
                    break

                # if we didnt find our char in the above range
                # we need to increase our current index by partition size
                curr += partition_size

        return "".join(res)

