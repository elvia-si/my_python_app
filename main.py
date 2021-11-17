from flask import Flask, request, Response, render_template

import json

app = Flask(__name__)

movie_db = {
    '1' : { 
        'name' : 'Stargate',
        'release_date' : '1994'  
    },
    '2' : {
        'name' : 'Sunshine',
        'release_date' : '2007' 
    },
    '3' : {
        'name' : 'The Holiday',
        'release_date' : '2006'  
    }
}

books_db = [
        {
            "author": "Chinua Achebe",
            "country": "Nigeria",
            "imageLink": "images/things-fall-apart.jpg",
            "language": "English",
            "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
            "pages": 209,
            "title": "Things Fall Apart",
            "year": 1958
        },
        {
            "author": "Dante Alighieri",
            "country": "Italy",
            "imageLink": "images/the-divine-comedy.jpg",
            "language": "Italian",
            "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
            "pages": 928,
            "title": "The Divine Comedy",
            "year": 1315
        },
        {
            "author": "Hans Christian Andersen",
            "country": "Denmark",
            "imageLink": "images/fairy-tales.jpg",
            "language": "Danish",
            "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
            "pages": 784,
            "title": "Fairy tales",
            "year": 1836
        },
        {
            "author": "Jane Austen",
            "country": "United Kingdom",
            "imageLink": "images/pride-and-prejudice.jpg",
            "language": "English",
            "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
            "pages": 226,
            "title": "Pride and Prejudice",
            "year": 1813
        },
        {
            "author": "Samuel Beckett",
            "country": "Republic of Ireland",
            "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
            "language": "French, English",
            "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
            "pages": 256,
            "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
            "year": 1952
        },
        {
            "author": "Giovanni Boccaccio",
            "country": "Italy",
            "imageLink": "images/the-decameron.jpg",
            "language": "Italian",
            "link": "https://en.wikipedia.org/wiki/The_Decameron\n",
            "pages": 1024,
            "title": "The Decameron",
            "year": 1351
        },
        {
            "author": "Jorge Luis Borges",
            "country": "Argentina",
            "imageLink": "images/ficciones.jpg",
            "language": "Spanish",
            "link": "https://en.wikipedia.org/wiki/Ficciones\n",
            "pages": 224,
            "title": "Ficciones",
            "year": 1965
        },
        {
            "author": "Albert Camus",
            "country": "Algeria, French Empire",
            "imageLink": "images/l-etranger.jpg",
            "language": "French",
            "link": "https://en.wikipedia.org/wiki/The_Stranger_(novel)\n",
            "pages": 185,
            "title": "The Stranger",
            "year": 1942
        }
    ]

def getBooks(arr):
    book_titles = []
    for item in arr:
        book_titles.append(item['title'])
    return book_titles


@app.route('/')
def home():
    books = getBooks(books_db)
    return render_template('index.html', books=books)




@app.route('/movie/add', methods=['POST'])
def addMovie():
    req_data = request.get_json()
    movie = req_data('movie')

    new_movie = {'4' : movie}
    movie_db.update(new_movie)
    return 'Movie added successfully'


#dialogare con il browser tramite il terminal
#per GET request
#curl localhost:PORT/movies jq

# per POST Request
# curl -X POST localhost/movie/add -d '{'movie' : {'name' : 'Matrix'}}' -H 'Content-Type: application/json'

# @app.route('/add-book', methods=['POST'])
# def addBook():
#     #...
#     return (request.form['something'])

@app.route('/hello')
def world():
    return '<h1>Hello world!!!</h1>'

@app.route('/movies')
def getMovies():
    html_response = '<ul>'
    for m in movie_db:
        html_response += '<li>' + movie_db[m]['name'] + '</li>'
    html_response += '</ul>'

    return html_response
    #return json.dumps(movie_db)



#READ

@app.route('/movies/<movie_id>', methods=['GET'])
def getMovie(movie_id):
    return json.dumps(movie_db[movie_id])



if __name__ == '__main__':
    app.run(host='127.0.0.1')