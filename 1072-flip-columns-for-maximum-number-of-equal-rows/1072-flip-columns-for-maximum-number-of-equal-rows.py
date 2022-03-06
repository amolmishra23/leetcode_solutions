import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
This question is equalvalent to "What is the maximum count of rows with same bit-patterns?". The bit-pattern here is defined as the bit-array and it's flipping. For example, [0,1,0,0] and [1,0,1,1] belong to the same bit-pattern.

This is becasue a group of rows with same bit-pattern can be transfered to rows of all 0's or 1's after certain column-flippings, therefore, the maximum number of rows with same bit-patterns equals to the maximum number of equal rows after column-flippings.

For example,
[
[ 0, 0, 0, 1 ]
[ 0, 1, 0, 0 ]
[ 1, 1, 0, 1 ]
[ 0, 1, 0, 0 ]
[ 1, 0, 1, 1 ]
]
has bit-patterns and number of appearances as:
[ 0, 0, 0, 1 ] <=> [ 1, 1, 1, 0 ] : 1
[ 0, 1, 0, 0 ] <=> [ 1, 0, 1, 1 ] : 3
[ 1, 1, 0, 1 ] <=> [ 0, 0, 1, 0 ] : 1
Therefore, the maximum possible rows with all 0's or 1's after certain column-flips are 3.
        """
        
        counter = collections.Counter()
        
        for row in matrix:
            temp = tuple(r^1 for r in row) if row[0]==1 else tuple(row)
            counter[temp]+=1
        
        return max(counter.values())