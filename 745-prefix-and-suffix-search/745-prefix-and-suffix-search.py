class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i,w in enumerate(words):
            l = len(w)
            for p in range(1, min(10, l) + 1):
                for s in range(1, min(10, l) + 1):
                    self.d[w[:p], w[-s:]] = i
            
    def f(self, p: str, s: str) -> int:
        return self.d[p, s] if (p, s) in self.d else -1