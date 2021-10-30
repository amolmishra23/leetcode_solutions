class Node:
    def __init__(self, start, end):
        """
        Apart storing the left, right nodes like usual tree.
        We also tend to store, which (start-end) nodes sum it includes. 
        And total is the sum of nodes from start-end
        """
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l>r: return None
            
            # this condition is for leaf node
            if l==r: 
                # we create a new node, whose child are none.
                # and assign its limits
                # and the sum
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = l + (r-l)//2
            
            # creating a new node. with limits, sum, and children. 
            root = Node(l, r)
            
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total

            # child node needs to be propogated up. (as it may be left/right child to some node above)
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def updateTree(root, i, val):
            # if after all the if-else waterfall, we finally end on start==end
            # it is the node to change value
            # hence we change value, and return it
            # to propogate to the entire tree
            if root.start == root.end:
                root.total = val
                return val
            
            # as its tree, like binary search to decide, which way do we go about??
            mid = (root.start + root.end) // 2
            
            # left or right side
            if i<=mid: updateTree(root.left, i, val)
            else: updateTree(root.right, i, val)
            
            # updating the total
            root.total = root.left.total + root.right.total
            
            # returning total to update along the way
            return root.total
        
        return updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def sumRangeTree(root, i, j):
            # again same like update condition
            if root.start == i and root.end == j: return root.total
            
            # to find which way do we travel
            mid = (root.start+root.end)//2
            
            # if solution is in left side
            if j<= mid: return sumRangeTree(root.left, i, j)
            
            # if solution is in right side
            elif i >= mid+1: return sumRangeTree(root.right, i, j)
            
            # solution is split in both sides. So we bound them by i,j and make function calls respectively
            # as (i, mid) and (mid+1, j)
            else:
                return sumRangeTree(root.left, i, mid) + sumRangeTree(root.right, mid+1, j)
            
        return sumRangeTree(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)