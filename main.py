class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
        
    def addbook(self, bookname):
        self.books.append(bookname)
        self.no_of_books+=1
    
    def shownumbers(self):
        print(f"The no. of books in the library is: {self.no_of_books}")
        
    def showbooks(self):
        if self.no_of_books==0:
            print("The library is empty")
        else:
            print("Books in Library")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}.{book}")

library1=Library()
library1.addbook("The MidNight Man")
library1.addbook("The Alchemist")
library1.showbooks()
library1.shownumbers()