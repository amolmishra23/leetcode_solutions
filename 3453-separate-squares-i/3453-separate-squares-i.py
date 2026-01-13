class Solution:
    def separateSquares(self, squares):
        L, R = 0.0, 1e9
        Ans = 0.0

        for _ in range(80):  # sufficient precision
            mid = L + (R - L) / 2.0
            LA, UA = 0.0, 0.0

            for _, y, l in squares:
                TA = l * l

                if y + l <= mid:
                    LA += TA                    # completely below
                elif y >= mid:
                    UA += TA                    # completely above
                else:
                    below = (mid - y) * l      # partially split
                    LA += below
                    UA += TA - below

            if LA >= UA:
                Ans = mid
                R = mid
            else:
                L = mid

        return Ans