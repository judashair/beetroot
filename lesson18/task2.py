class Person:
    def __init__(self, id_, name, company):
        self.id_ = id_
        self.name = name
        self.company = company

    def __str__(self):
        return f"{self.id_}, {self.name}, {self.company}"

    def __repr__(self):
        return f"{self.id_}, {self.name}, {self.company}"


class Boss(Person):
    def __init__(self, id_, name, company):
        super().__init__(id_, name, company)
        self._workers = []

    @property
    def add_workers(self):
        return self._workers

    @add_workers.setter
    def add_workers(self, prop_worker):
        if isinstance(prop_worker, Worker):
            self._workers.append([prop_worker])
            print(self._workers)
        else:
            raise AttributeError(f"{prop_worker} is not an instance of Worker!")


class Worker(Person):
    def __init__(self, id_, name, company, boss):
        super().__init__(id_, name, company)
        if isinstance(boss, Boss):
            self.boss = boss
        else:
            raise AttributeError(f"{boss} is not an instance of Boss!")

    @property
    def check_boss(self):
        return self.boss

    @check_boss.setter
    def check_boss(self, prop_boss):
        if isinstance(prop_boss, Boss):
            self.boss = prop_boss
        else:
            raise AttributeError(f"{prop_boss} is not an instance of Boss!")
        print(self.boss)


boss_s = Boss(1, "Anna", "Samsonenko")
worker_s_1 = Worker(11, "Andrii", "Beetroot", boss_s)
worker_s_2 = Worker(12, "Anastasiia", "Beetroot", boss_s)

boss_k = Boss(2, "Andrii", "Kondratyuk")
worker_k_1 = Worker(21, "Ira", "Beetroot", boss_k)
worker_k_2 = Worker(22, "Dima", "Beetroot", boss_k)
worker_k_3 = Worker(23, "Oliia", "Beetroot", boss_k)

try:
    boss_s.add_workers = worker_s_1
    boss_s.add_workers = worker_s_2

    worker_s_2.check_boss = worker_s_1

    boss_k.add_workers = boss_s
    boss_k.add_workers = worker_k_1
    boss_k.add_workers = worker_k_2
    boss_k.add_workers = worker_k_3
except AttributeError as error_msg:
    print(error_msg)

