class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"Book Name:{self.title} \nAuthor   :{self.author}\nisbn     :{self.isbn}")
book1=Book('Looking for Life','A Legend',8646)
book1.display()