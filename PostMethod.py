from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': '1st Book'},
    {'title': 'Title Seven', 'author': 'Author One', 'category': '2'},
    {'title': 'Title Eight', 'author': 'Author One', 'category': '3'},
    {'title': 'Title Nine', 'author': 'Author One', 'category': '4'},
    {'title': 'Title Ten', 'author': 'Author One', 'category': '5'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
def first_api():
    return BOOKS


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put("/books/updateBook")
def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold() == updated_book.get('title').casefold()):
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/books/assignment')
def all_books(author_name: str):
    book_titles=[]
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('author').casefold()==author_name.casefold()):
            book_titles.append(BOOKS[i].get('title')+": "+BOOKS[i].get('category'))
    return book_titles

@app.get("/books/{book_author}/")
def read_data_Author(book_author: str):
    book_titles=[]
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('author').casefold()==book_author.casefold()):
            book_titles.append(BOOKS[i].get('title')+": "+BOOKS[i].get('category'))
    return book_titles   