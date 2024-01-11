import time
sd = time.time()
class SimpleRandomGenerator:
    def __init__(self, seed=sd):
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return int(self.seed)

# Example usage:
rng = SimpleRandomGenerator()
for _ in range(5):
    print(rng.generate())
