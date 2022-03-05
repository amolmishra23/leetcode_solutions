class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        """
        A=[1,3] B=[2]
        
        sum(A)=4
        sum(B)=2
        diff = (4-2)//2 = 1
        
        We need to subtract 1 from A/add 1 to B
        Exchange is must. 1 I give to A, and get back from B
        Ideally, if we have 1, A could give B. And both would be at 3,3
        But for exchange to happen,
        for each element in A, we try to find, if we give that to B, do we have a balancing element from B
        
        1 in A
        1-1 in B? 0 not in B
        3-1 in B? 2 in B
        
        So give 3 to B, and get 2 from B
        Hence solved. 
        """
        
        diff = (sum(A) - sum(B)) // 2
        b = set(B)
        for x in A:
            if x - diff in b:
                return [x, x - diff]
        return []