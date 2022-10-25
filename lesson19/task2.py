class Range:

    def __init__(self, start, stop, step):
        self.step = step
        self.stop = stop
        self.start = start

    def __iter__(self):
        self.start -= self.step
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        raise StopIteration


a = Range(0, 100, 11)
for i in a:
    print(i)
