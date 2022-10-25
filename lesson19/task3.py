class People:

    def __init__(self, iterable: str, ind=0):
        self.iterable = iterable
        self.ind = ind

    def __iter__(self):
        print(f"Зараз на планеті проживає {len(self.iterable[self.ind:])} мільярдів людей.")
        return self

    def __next__(self):
        if self.ind < len(self.iterable):
            old_ind = self.ind
            self.ind += 1
            return f"10 років тому було {len(self.iterable[old_ind:])} мільярди людей."
        else:
            print(f"І нікого не стало.")
            raise StopIteration


a = People("12345678", 0)
for i in a:
    print(i)
