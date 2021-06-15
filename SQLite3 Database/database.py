#Concerned with sorting and retrieving books from a list.
from .database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    #IF NOT EXISTS only creates table if not existing
    #table name(column, column, column)
    #column  - column name/ data type/ key

def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))
    #inserts question marks as the respective parameters: name and author

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    #collect all the columns from the cursor execute
    #import the cursor selected rows into books using fetch [(name, author, read), (name, author, read)]
    return books

def mark_book_as_read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_name,))

def remove_book(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (book_name,))