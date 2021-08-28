class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def solve(needs):
            if tuple(needs) in self.cache: return self.cache[tuple(needs)]
            
            # we need to find the best cost for needs! 
            cost = 0
            # calculating the worst case
            for i in range(len(needs)):
                cost += needs[i]*price[i]
                
            # lets iterate over all the special offers
            for i in range(len(special)):
                # can we use this special offer?
                # provided we need atleast that much qty of each item. 
                for j in range(len(needs)):
                    if needs[j]<special[i][j]: break
                else:
                    # if we didnt break out anywhere, and all needs are more than the special offer.
                    new_needs = [needs[k]-special[i][k] for k in range(len(needs))]
                    cost = min(cost, special[i][-1]+solve(new_needs))
            
            self.cache[tuple(needs)] = cost
            return cost
        
        
        self.cache={}
        return solve(needs)