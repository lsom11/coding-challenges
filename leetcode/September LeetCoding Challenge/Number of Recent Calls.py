class RecentCounter:
    def __init__(self):
        self.calls = deque()

    def ping(self, t):
        self.calls.append(t)
        while self.calls[0] < self.calls[-1] - 3000:
            self.calls.popleft()
        return len(self.calls)