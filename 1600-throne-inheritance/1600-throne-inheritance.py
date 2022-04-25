class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nation = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.nation[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        self.dfs(self.king)
        return self.ans
    
    def dfs(self, cur):
        if cur not in self.dead:
            self.ans.append(cur)
        for child in self.nation[cur]:
            self.dfs(child)