class Fancy(object):

    def __init__(self):
        self.mod = 10**9 + 7
        self.seq = []
        # Represents the current global transformation: val * a + b
        self.a = 1 
        self.b = 0

    def append(self, val):
        # We need to store val such that: (stored_val * current_a) + current_b = val
        # Therefore: stored_val = (val - current_b) * inv(current_a)
        inv_a = pow(self.a, self.mod - 2, self.mod)
        self.seq.append(((val - self.b) * inv_a) % self.mod)

    def addAll(self, inc):
        # Updates the global increment: (x * a + b) + inc => x * a + (b + inc)
        self.b = (self.b + inc) % self.mod

    def multAll(self, m):
        # Updates the global state: (x * a + b) * m => x * (a * m) + (b * m)
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        # Apply the current global transformation to the stored value
        return (self.seq[idx] * self.a + self.b) % self.mod
