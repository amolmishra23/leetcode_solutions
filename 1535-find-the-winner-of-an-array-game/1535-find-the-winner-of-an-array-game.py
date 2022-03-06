class Solution:
    def getWinner(self, A, k):
        cur = A[0]
        win = 0
        for i in range(1, len(A)):
            # just need to verify if any index can have a winning streak of k
            # if the next element defeats it, we will reset the counter anyways. 
            if A[i] > cur:
                cur = A[i]
                win = 0
            win += 1
            if (win == k): break
        return cur