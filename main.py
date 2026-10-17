from books import show_books

name = input("Enter your name: ")
print("Welcome", name)

count = int(input("How many books do you want to add? "))
books = []

for i in range(count):
    book = input("Enter book: ")
    books.append(book)

show_books(books)
