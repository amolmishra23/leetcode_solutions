class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(('+' in s) - ('-' in s) for s in operations)