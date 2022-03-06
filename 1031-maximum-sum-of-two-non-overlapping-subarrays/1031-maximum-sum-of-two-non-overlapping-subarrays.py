class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # 1. Build a presum array from A to find the sum of a range in O(1) time
        A = [0] + A + [0]
        for i in range(1, len(A)):
            A[i] += A[i-1]

        # 2. For each index i, record the largest array of size L or M that is to the LEFT of index i (NOT including i)
        l_left = [0]
        m_left = [0]
        for i in range(1, len(A)):
            l_left.append(max(l_left[-1], A[i] - A[i-L]) if i >= L else 0)
            m_left.append(max(m_left[-1], A[i] - A[i-M]) if i >= M else 0)
        

        # 3. For each index i, record the largest array of size L or M that is to the RIGHT of index i (including i)
        l_right = [0]*len(A)
        m_right = [0]*len(A)
        for i in range(len(A) - 2, -1, -1):
            l_right[i] = max(l_right[i+1], A[i+L] - A[i] if i + L < len(A) else 0)
            m_right[i] = max(m_right[i+1], A[i+M] - A[i] if i + M < len(A) else 0)

        # 4. Return the largest combination of (l_left[i] and m_right[i]) OR (l_right[i] and m_left[i])
        return max(max(l_left[i] + m_right[i], l_right[i] + m_left[i]) for i in range(1, len(A) - 1))