import collections
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        coins = [20, 10, 5]
        counts = collections.defaultdict(int)
        for bill in bills:
            counts[bill]+=1
            change = bill - 5
            
            
            for coin in coins:
                if change==0: break
                if change>=coin:
                    no_of_coin = min(counts[coin], change//coin)
                    counts[coin]-=no_of_coin
                    change -= coin*no_of_coin
            if change!=0:
                return False
        
        return True