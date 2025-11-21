class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.i+1]
        self.history.append(url)
        self.i = len(self.history) - 1

    def back(self, steps: int) -> str:
        access_idx = self.i - steps
        if access_idx < 0: access_idx = 0
        self.i = access_idx
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        total_steps = self.i + steps
        if total_steps > len(self.history)-1: total_steps = len(self.history)-1
        self.i = total_steps
        return self.history[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)