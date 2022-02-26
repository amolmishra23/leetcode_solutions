class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if (jug1Capacity + jug2Capacity) < targetCapacity:
            return False
        queue = [0]
        visited = {0}
        while len(queue) > 0:
            node = queue.pop(0)
            for step in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
                total = node + step
                if total == targetCapacity:
                    return True
                if total < 0 or total > jug1Capacity+jug2Capacity:
                    continue
                if total not in visited:
                    queue.append(total)
                    visited.add(total)
        return False