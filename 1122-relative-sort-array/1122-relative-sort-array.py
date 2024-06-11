class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)
    
    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_set, arr2_set, count = set(arr1), set(arr2), Counter(arr1)
        diff, res = sorted(arr1_set.difference(arr2_set)), []
        for x in arr2+diff: res.extend([x]*count[x])
        return res