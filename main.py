from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from config import Config

#import json

app = Flask(__name__, instance_relative_config=False)



app.config.from_object(Config)

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    author = db.Column(db.VARCHAR(length=255))
    title = db.Column(db.VARCHAR(length=255))
    year = db.Column(db.Integer)

# GET HTTP VERB

@app.route('/')
def getBooks():
    books = Book.query.all()
    return render_template('index.html', books=books)

# POST HTTP VERB

@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title') 
        year = request.form.get('year')

        new_book = Book(author=author, title=title, year=int(year))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('getBooks'))
    return render_template('add-book.html')

#GET A SINGLE BOOK

@app.route("/book/<book_id>")
def get_book(book_id):
    book = Book.query.get(book_id)
    return render_template('book-detail.html', book=book)

# PATCH VERB UPDATE BOOK
@app.route("/book/update/<book_id>",  methods=["GET", "POST"])
def update(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if request.method == 'POST':
        newauthor = request.form.get("newauthor")
        newtitle = request.form.get("newtitle")
        newyear = request.form.get("newyear")
        if newauthor:
            book.author = newauthor
        if newtitle:
            book.title = newtitle
        if newyear:
            book.year = newyear
        db.session.commit()
        return redirect(url_for('getBooks'))
    return render_template('edit-book.html', book=book)



#DELETE HTTP VERB
@app.route("/book/delete/<book_id>")
def deleteBook(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('getBooks'))


@app.route('/hello')
def world():
    return '<h1>Hello world!!!</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1')