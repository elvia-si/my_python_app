from flask import Flask, request, render_template, redirect, url_for

from pymongo import MongoClient

#import json

app = Flask(__name__, instance_relative_config=False)

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'your_database',
#     'host': 'MONGODB_HOST',
#     'port': 27017
# }

client = MongoClient('MONGODB_HOST', 27017)

db = client.books_db
books = db.books

# GET HTTP VERB

@app.route('/')
def getBooks():
    books = books.find()
    return render_template('index.html', books=books)

# POST HTTP VERB

@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title') 

        new_book = books(author=author, title=title)
        books.insert_one(new_book)
        return redirect(url_for('getBooks'))
    return render_template('add-book.html')

#GET A SINGLE BOOK

@app.route("/book/<book_id>")
def get_book(book_id):
    book = books.findOne(book_id)
    return render_template('book-detail.html', book=book)

# PATCH VERB UPDATE BOOK
@app.route("/book/update/<book_id>",  methods=["GET", "POST"])
def update(book_id):
    book = books.findOne(id=book_id)
    if request.method == 'POST':
        newauthor = request.form.get("newauthor")
        newtitle = request.form.get("newtitle")
        if newauthor:
            book.author = newauthor
        if newtitle:
            book.title = newtitle
        return redirect(url_for('getBooks'))
    return render_template('edit-book.html', book=book)



#DELETE HTTP VERB
@app.route("/book/delete/<book_id>")
def deleteBook(book_id):
    book = books.findOne(id=book_id)
    if book:
        books.delete_one(book)
    return redirect(url_for('getBooks'))


@app.route('/hello')
def world():
    return '<h1>Hello world!!!</h1>'


if __name__ == '__main__':
    app.run(debug=True)