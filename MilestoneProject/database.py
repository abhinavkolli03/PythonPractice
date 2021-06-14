#Concerned with sorting and retrieving books from a list.
import json

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    update_files()

def show_list():
    for book in books:
        print(f"'{book['name']}' by {book['author']}, read: {book['read']}")
    update_files()

def read_book(book_name):
    for book in books:
        if book['name'] == book_name:
            print("Book found!")
            book['read'] = True
            break
    update_files()

def remove_book(book_name):
    new_books = []
    for book in books:
        if book['name'] == book_name:
            books.remove(book)
    update_files()

def update_files():
    bookstore = open('bookstore.txt', 'w')
    json.dump(books, bookstore)
    bookstore.close()