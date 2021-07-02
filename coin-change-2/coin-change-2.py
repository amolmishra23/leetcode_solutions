class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def coin_change(coins, target, idx):
            if (target, idx) in cache: return cache[(target, idx)]
            if target==0: return 1
            if target<0: return 0
            if idx>=len(coins): return 0

            res = 0
            res += coin_change(coins, target-coins[idx], idx)
            res += coin_change(coins, target, idx+1)
            cache[(target, idx)] = res
            return res

        cache={}
        return coin_change(coins, amount, 0)