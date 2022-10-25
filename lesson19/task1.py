class EnumerateWithIndex:

    def __init__(self, _iterable, _from=0):
        self._iterable = _iterable
        self._from = _from
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self._iterable):
            raise StopIteration
        else:
            result = self._from, self._iterable[self.index]
            self.index += 1
            self._from += 1
        return result


a = "Beetroot Academy"
for i in EnumerateWithIndex(a, 1):
    print(i, end=" ")
