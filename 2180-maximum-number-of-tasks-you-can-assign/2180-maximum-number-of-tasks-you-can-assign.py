class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort(); workers.sort()
        l, r = 0, min(len(tasks), len(workers))

        while l<r:
            m = (l+r+1)//2
            pillsUsed = 0
            # mid to large workers
            available = workers[-m:]
            canAssign = True

            # mid size to small size tasks
            for t in reversed(tasks[:m]):
                if available[-1] >= t:
                    available.pop()
                else:
                    idx = bisect.bisect_left(available, t-strength)
                    if idx == len(available) or pillsUsed == pills:
                        canAssign = False
                        break
                    pillsUsed += 1
                    available.pop(idx)

            if canAssign: l = m
            else: r = m-1

        return l