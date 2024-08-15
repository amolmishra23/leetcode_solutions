class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = Counter()
        coins = [20,10,5]
        
        for bill in bills:
            count[bill] += 1
            change = bill - 5
            
            for coin in coins:
                if change==0: break
                if change>=coin:
                    final_coins = min(change//coin, count[coin])
                    count[coin] -= final_coins
                    change -= coin*final_coins
                    
            if change!=0: return False
            
        return True
            