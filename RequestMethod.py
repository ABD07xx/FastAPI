from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


#Basic Get
@app.get("/")
def second_api():
    return "Hello"


#Returning all Books
@app.get("/books")
def first_api():
    return BOOKS

#Retruning a Key Value Pair
@app.get("/books/mybook")
def read_all_books():
    return {'book_title':'My favourtie Book'}


#Dynamic URL Building with space changing to %20
@app.get("/books/{dynamic_param}")
def read_all_books(dynamic_param):
    return {'dynamic_param':dynamic_param}


#Dynamic URL to fetch details using Book Titles use docs to fetch 
@app.get("/books/{book_title}")
def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('/books/')
def read_category(category: str):
    books_return = []
    for i in BOOKS:
        if i.get('category').casefold() == category.casefold():
            books_return.append(i)
    return books_return


@app.get("/books/{book_author}/")
def read_category(book_author: str,category: str):
    book_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            book_return.append(book)
    return book_return