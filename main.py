class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return self.title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        reserve_list = []
        for b in self.books:
            if b.title != book.title and b.author != book.author:
                reserve_list.append(b)
        self.books = reserve_list

    def search_books(self, search_string):
        match_list = []
        
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                match_list.append(book)
        return match_list


book1 = Book("Women of Owu", "Prof. Femi Osofisan")
book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie")
book3 = Book("A Woman in her prime", "Asare Konadu")
book4 = Book("Half of a yellow Sun", "Chimamanda Ngozi Adichie")
book5 = Book("The Joys of Motherhood", "Buchi Emecheta")
print(book1.get_title())

wale_lab = Library("Wale_Lab")
wale_lab.add_book(book1)
wale_lab.add_book(book2)
wale_lab.add_book(book3)
wale_lab.add_book(book4)
wale_lab.add_book(book5)
print(wale_lab.search_books("Woman"))