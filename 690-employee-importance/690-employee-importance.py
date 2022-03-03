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
    
    def getImportance(self, employees: List['Employee'], idx: int) -> int:
        id_to_emp = {emp.id: emp for emp in employees}
        
        def dfs(idx):
            sub_sum = sum([dfs(x) for x in id_to_emp[idx].subordinates])
            return sub_sum + id_to_emp[idx].importance
        
        return dfs(idx)