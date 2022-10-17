class Author:

    def __init__(self, first_name, last_name, birt_date, country):
        self.country = country
        self.birt_date = birt_date
        self.last_name = last_name
        self.first_name = first_name
        self.books = []

    def new_book(self, name, year):
        book = Book(name, year, self)
        self.books.append(book)
        return book

    def __str__(self):
        return f"Author {self.first_name} {self.last_name} written {self.books}, {len(self.books)} books!"

    def __repr__(self):
#         return f"{self.first_name} {self.last_name}"
          return f"Author('{self.first_name}', '{self.last_name}')"


class Book:
    books_counter = 0

    def __init__(self, name, year, author: "Author"):
        self.author = author
        self.year = year
        self.__name = name
        self.__class__.books_counter += 1

    def __repr__(self):
        # return f"{self.__name}"
        return f"Book('{self.author}', '{self.year}', '{self.__name}')"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def add_book(self, book: Book):
        self.books.append(book)
        self.authors.append(book.author)

    def add_author(self,):
        pass

    def group_by_author(self, author: Author):
        return author.__str__()

    def group_by_year(self, year: str):
        year_list = []
        for book in self.books:
            if year in book.year:
                year_list.append(book)
        return year_list

    def __str__(self):
        return f"In the library {self.name} are {len(self.books)} books: {self.books}"

    def __repr__(self):
        # return self.__str__()
        return f"Library('{self.library}')"


lib1 = Library("Vivat")
aut = Author("Kate", "Russell", "18.04.1995", "Ukraine")
aut1 = Author("Gillian", "Flynn", "11.03.1996", "USA")
aut2 = Author("Paul", "Tobin", "13.10.1502", "UK")

vb1 = aut1.new_book("Dark Vanessa", "2021")
vb2 = aut1.new_book("Naruto", "2002")
db1 = aut.new_book("Fighter club", "2016")
db2 = aut.new_book("The Devil in the White City", "2021")
sb1 = aut2.new_book("The Witcher: Dark Horse", "2021")
sb2 = aut2.new_book("The Witcher: Dark Horse 2", "2022")

lib1.add_book(vb1)
lib1.add_book(vb2)
lib1.add_book(db1)
lib1.add_book(db2)
lib1.add_book(sb1)
lib1.add_book(sb2)

print(lib1.group_by_author(aut2))
print(lib1.group_by_year("2002"))
print(lib1)
