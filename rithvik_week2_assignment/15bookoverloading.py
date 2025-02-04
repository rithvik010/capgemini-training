class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def get_author(self):
        return self.author
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"
    def __add__(self, other):
        return BookSeries(self, other)
class BookSeries:
    def __init__(self, book1, book2):
        self.books = [book1, book2]
    def __str__(self):
        book_series_str=""
        for book in self.books:
            book_series_str+=str(book)+"\n"
            return book_series_str
        def __add__(self,other):
            self.books.append(other)
            return self
        
def main():
    books=[]
    while True:
        print("1. Add new Books: ")
        print("2. Check books list ")
        print("3. exit")
        choice=int(input("Enter the operation needed: "))
        if choice==1:
            title=input("enter book title:")
            author=input("enter authors name:")
            isbn=input("enter ISBN:")
            new_book=Book(title,author,isbn)
            books.append(new_book)
        elif choice==2:
            for book in books:
                print(book)
        elif choice==3:
            exit()

main()