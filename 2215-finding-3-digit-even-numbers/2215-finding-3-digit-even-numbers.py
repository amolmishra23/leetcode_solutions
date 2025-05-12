class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n, store = len(digits), SortedList()

        for i in range(n):
            if not digits[i]: continue
            for j in range(n):
                if i==j: continue
                for k in range(n):
                    if j==k or k==i or digits[k]%2: continue
                    s = str(digits[i]) + str(digits[j]) + str(digits[k])
                    if int(s) not in store: store.add(int(s))

        return list(store)