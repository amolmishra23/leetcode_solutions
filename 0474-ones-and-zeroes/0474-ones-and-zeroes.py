class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        costs = []

        for s in strs:
            costs.append((s.count("0"), s.count("1")))

        res =[[[None for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]
        def dp(i, m_rem, n_rem):
            if res[i][m_rem][n_rem] is not None: return res[i][m_rem][n_rem]
            if i==len(costs): return 0

            res_skip, res_take = dp(i+1, m_rem, n_rem), 0
            zeros, ones = costs[i]
            if m_rem >= zeros and n_rem >= ones:
                res_take = 1 + dp(i+1, m_rem-zeros, n_rem-ones)

            res[i][m_rem][n_rem] = max(res_skip, res_take)
            return res[i][m_rem][n_rem]

        return dp(0,m,n)