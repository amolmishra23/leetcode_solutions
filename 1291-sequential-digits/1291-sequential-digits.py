class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        # trying every possible such number. 
        queue = deque(range(1, 10))
        
        while queue:
            elem = queue.popleft()
            
            # this might be potential result candidate
            if low<=elem<=high: res.append(elem)
            last = elem%10
            
            # if the last digit is less than 9, we can add a new digit. 
            # after traversing 123, we can make it as 1234 and add to queue as a potential choice. 
            # if 1234 later doesnt get used anyways, its not included in res. 
            if last<9: queue.append(elem*10 + last + 1)
                
        return res