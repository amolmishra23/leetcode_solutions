"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    """
    Very easy question.
    First requirement is to make it tree like, where traversing can be easy
    Hence make all the data in a hashmap
    Then just basic dfs we do, to traverse the entire employee chain for finding their importance
    """
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map_ = {emp.id: emp for emp in employees}
        
        def dfs(id):
            child_imp = sum(dfs(x) for x in map_[id].subordinates)
            return child_imp + map_[id].importance
        
        return dfs(id)