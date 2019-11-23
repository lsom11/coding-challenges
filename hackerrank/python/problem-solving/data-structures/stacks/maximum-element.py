class Stack:
    def __init__(self):
        self.stack = []
        self.max_nums = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_nums or val >= self.max_nums[-1]:
            self.max_nums.append(val)

    def pop(self):
        popped_num = self.stack.pop()
        # pop from max stack if it's the same num

        if popped_num == self.max_nums[-1]:
            self.max_nums.pop()

    def get_max(self):
        print(self.max_nums[-1])


s = Stack()
N = int(input())
for _ in range(N):
    command = input().split(' ')
    if command[0] == '1':
        s.push(int(command[1]))
    elif command[0] == '2':
        s.pop()
    else:
        s.get_max()
