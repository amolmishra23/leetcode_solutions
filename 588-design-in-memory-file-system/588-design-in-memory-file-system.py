class FileSystem:

    def __init__(self):
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        if len(path)==1: return sorted(self.trie.keys())
        
        path = path.split("/")
        node = self.trie
        
        for p in path[1:]:
            node = node.setdefault(p, {})
        
        if type(node)==str: return [path[-1]]
        
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        path = path.split("/")
        node = self.trie
        
        for p in path[1:]:
            node = node.setdefault(p, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")
        file = path[-1]
        node = self.trie
        
        for p in path[1:-1]:
            node = node.setdefault(p, {})
            
        if file not in node:
            node[file] = content
        else:
            node[file]+= content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")
        node = self.trie
        
        for p in path[1:-1]:
            node = node.setdefault(p, {})
            
        return node[path[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)