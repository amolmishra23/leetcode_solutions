# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._hasNext, self.buffer, self.gen = True, None, self.flatten(nestedList)
        self.next()
    
    def flatten(self, object):
        for item in object:
            if item.isInteger(): yield item.getInteger()
            else: yield from self.flatten(item.getList())
    
    def next(self) -> int:
        try:
            v = self.buffer
            self.buffer = self.gen.__next__()
        except StopIteration:
            self._hasNext = False
        return v
            
    def hasNext(self) -> bool:
        return self._hasNext 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())