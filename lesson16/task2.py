class Mathematician:

    def square_nums(self, list_of_numbers: list):
        return [number*number for number in list_of_numbers]

    def remove_positives(self, list_of_numbers: list):
        for number in list_of_numbers:
            if number > 0:
                list_of_numbers.remove(number)
        return list_of_numbers

    def filter_leaps(self, list_of_numbers: list):
        list_of_numbers_2 = []
        for number in list_of_numbers:
            if number % 4 != 0 or (number % 100 == 0 and number % 400 != 0):
                pass
            else:
                list_of_numbers_2.append(number)
        return list_of_numbers_2


m = Mathematician()
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print( m.filter_leaps([2001, 1884, 1995, 2003, 2020]))