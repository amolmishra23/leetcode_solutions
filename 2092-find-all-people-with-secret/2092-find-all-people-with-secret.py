class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: x[2])
        byTime = itertools.groupby(meetings, key = lambda x: x[2])

        known = {0,firstPerson}
        for _, meeting in byTime:
            queue = set()
            graph = defaultdict(list)

            for a,b,_ in meeting:
                graph[a].append(b); graph[b].append(a)
                if a in known: queue.add(a)
                if b in known: queue.add(b)

            queue = deque(queue)

            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in known:
                        known.add(neigh)
                        queue.append(neigh)

        return list(known)