class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        lookup, result = {}, []
        """
        Go over the restaurants in for loop.
        Verify all the conditions. 
        If it has matched, cache the restaurant id and current index in array
        And store in res.
        
        Before returning we need to sort the res, by rating -> id.
        Return the result.
        """
        for j, (i, r, v, p, d) in enumerate(restaurants):
            if v>=veganFriendly and p<=maxPrice and d<=maxDistance: # if the conditions are satisfied
                lookup[i] = j # we store the info of restaurant id i, whose details are at index j in restaurants list. 1 level filter is done. 
                result.append(i) # we also save the restaurant id in our result. 
        
        # now to return stuff in proper sorted order, we also need j. Hence we had stored it
        result.sort(key = lambda x: (-restaurants[lookup[x]][1], -restaurants[lookup[x]][0]))
        return result