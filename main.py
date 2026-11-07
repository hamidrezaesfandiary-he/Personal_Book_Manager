from books import show_books, load_books, save_books
from dotenv import load_dotenv
import os

load_dotenv()
name = input("Enter your name: ")

admin_mode = input("do you want to open admin mode? (yes/no): ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")

print("Welcome", name)

count = int(input("How many books do you want to add? "))
books = []

for i in range(count):
    book_name = input("Enter book: ")
    books.append(book_name)
    priority = input("enter priority(low, medium, high): ").lower()
    book = {
        "name": book_name, 
        "priority": priority
    }
    books.append(book)

save_books(books)
show_books(books)