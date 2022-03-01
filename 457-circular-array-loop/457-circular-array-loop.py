class Solution:
    def circularArrayLoop(self, arr: List[int]) -> bool:
        def find_next(arr, idx, dir):
            curr_dir = arr[idx]>=0
            if curr_dir != dir: return -1
            
            next_idx = (idx+arr[idx])%len(arr)
            
            if next_idx<0: next_idx += len(arr)
                
            if idx==next_idx: return -1
            
            return next_idx
            
        
        for i in range(len(arr)):
            slow, fast = i, i
            dir = arr[i]>=0
            
            while True:
                slow = find_next(arr, slow, dir)
                if slow == -1: break
                    
                fast = find_next(arr, fast, dir)
                if fast == -1: break
                    
                fast = find_next(arr, fast, dir)
                if fast == -1: break
                    
                if slow==fast: return True

        return False
                