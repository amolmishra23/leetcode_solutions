class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        l1, l2 = v1.split("."), v2.split(".")
        length = max(len(l1), len(l2))

        for i in range(length):
            v1 = int(l1[i]) if i<len(l1) else 0
            v2 = int(l2[i]) if i<len(l2) else 0
            if v1<v2:
                return -1
            if v1>v2:
                return 1

        return 0