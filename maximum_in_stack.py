class MaxStack:
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.maxes = []

    def push(self, val):
        # Fill this in.
        self.stack.append(val)
        if not self.maxes:
            self.maxes.append(val)
        else:
            self.maxes.append(max(val, self.maxes[-1]))

    def pop(self):
        # Fill this in.
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        # Fill this in.
        return self.maxes[-1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
