class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book): # method to add the book
    self.books.append(book) # this will append the book
    self.noBooks = len(self.books) # check

  def showInfo(self):
    print(f"The library has {self.noBooks} books.")
    # print("The books are ->")
    # for book in self.books:
    #   print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()