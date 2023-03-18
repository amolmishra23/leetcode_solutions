class BrowserHistory:

    def __init__(self, homepage: str):
        self.history, self.future = deque([homepage]), deque()

    def visit(self, url: str) -> None:
        self.history.append(url); self.future.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.history)>1:
            self.future.append(self.history.pop())
            steps-=1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps and len(self.future)>0:
            self.history.append(self.future.pop())
            steps-=1
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)