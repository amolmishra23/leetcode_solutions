class StringIterator:

    def __init__(self, compressedString: str):
        self.tokens = deque()
        for token in re.findall('\D\d+', compressedString):
            self.tokens.append((token[0], int(token[1:])))

    def next(self) -> str:
        if not self.tokens: return " "
        token, count = self.tokens.popleft()
        if count>1:
            self.tokens.appendleft((token, count-1))
        return token

    def hasNext(self) -> bool:
        return bool(self.tokens)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()