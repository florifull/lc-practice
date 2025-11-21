class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.end = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        self.end = self.curr
        
    def back(self, steps: int) -> str:
        access_idx = self.curr - steps
        if access_idx < 0: access_idx = 0
        self.curr = access_idx
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        access_idx = self.curr + steps
        if access_idx > self.end: access_idx = self.end
        self.curr = access_idx
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)