from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to marks a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICE)
    if user_input != 'q':
        return user_input
    return "end"

def prompt_add_book():
    book_name = input("Enter book name: ")
    book_author = input("Enter book author: ")
    database.add_book(book_name, book_author)

def list_books():
    database.show_list()

def prompt_read_book():
    find_book = input("Which book have you read: ")
    database.read_book(find_book)

def prompt_delete_book():
    delete_book = input("Which book would you like to remove: ")
    database.remove_book(delete_book)

user_input = menu()
while user_input != 'end':
    if user_input == 'a':
        prompt_add_book()
    elif user_input == 'l':
        list_books()
    elif user_input == 'r':
        prompt_read_book()
    elif user_input == 'd':
        prompt_delete_book()
    print("Continue your bookstore experience!")
    user_input = menu()

print("Thank you for using our bookstore!")

# def prompt_add_book() ask for the book name and author
# def list_books() show all the books in our list
# def prompt_read_book() ask for book name and change it to "read" in our list
# def prompt_delete_book() ask for book name and remove book from list
