class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        nodes, count = deque([root]), 0
        
        def perm(arr):                                            # this function simulates cycle sort,
            pos = {m:j for j,m in enumerate(sorted(arr))}         # namely, traverses every cycle in
            vis, tot = [0] * len(arr), 0                          # the permutation of elements and 
            for i in range(len(arr)):                             # counts the number of swaps 
                cnt = 0
                while not vis[i] and i != pos[arr[i]]:            # it is known that cycle sort is the
                    vis[i], i = 1, pos[arr[i]]                    # sorting algorithm with the minmal
                    cnt += 1                                      # number of memory operations (swaps)
                tot += max(0, cnt-1)                              # needed to sort an array
            return tot
                    
        while nodes:
            vals = []
            for _ in range(len(nodes)):                            # [1] this code performs a level-by-level
                n = nodes.popleft()                                #     BFS scan of the tree and extracts
                vals.append(n.val)                                 #     a list of values 'vals' for each level
                if n.left  : nodes.append(n.left)
                if n.right : nodes.append(n.right)
            count += perm(vals)                                    # [2] each level is sorted independently
            
        return count