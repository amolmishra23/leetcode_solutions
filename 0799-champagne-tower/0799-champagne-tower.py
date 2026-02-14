class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]

        for i in range(query_row):
            next_row = [0.0] * (len(row)+1)

            for j in range(len(row)):
                overflow = row[j]-1.0

                if overflow>0:
                    next_row[j] += overflow/2.0
                    next_row[j+1] += overflow/2.0

            row = next_row

        return min(1.0, row[query_glass])