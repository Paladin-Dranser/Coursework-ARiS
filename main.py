from flask import Flask, render_template, url_for, request, redirect
import mysql.connector as mariadb


mariadb_connection = mariadb.connect(
    user='flask_user',
    password='password',
    database='flask_coursework'
)

def get_books_by_genre(genre):
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT books.name, books.pdf_link, books.image_link, \
        authors.name, genres.name \
        FROM genres \
        JOIN books_genres ON genres.id = books_genres.genre_id \
        JOIN books ON books_genres.book_id = books.id \
        JOIN books_authors ON books.id = books_authors.book_id \
        JOIN authors ON books_authors.author_id = authors.id \
        WHERE genres.name = %s", (genre,)
    )

    books_info = cursor.fetchall()
    cursor.close()

    return books_info


def search_by_book(book_name):
    book_name = '%' + book_name + '%'
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT books.name, books.pdf_link, books.image_link, \
        authors.name, genres.name \
        FROM books \
        JOIN books_authors ON books.id = books_authors.book_id \
        JOIN authors ON books_authors.author_id = authors.id \
        JOIN books_genres ON books.id = books_genres.book_id \
        JOIN genres ON books_genres.genre_id = genres.id \
        WHERE LOWER(books.name) LIKE LOWER(%s)", (book_name,)
    )

    books_info = cursor.fetchall()
    cursor.close()

    return books_info

def search_by_author(author):
    author = '%' + author + '%'
    cursor = mariadb_connection.cursor()

    cursor.execute("SELECT books.name, books.pdf_link, books.image_link, \
        authors.name, genres.name \
        FROM authors \
        JOIN books_authors ON authors.id = books_authors.author_id \
        JOIN books ON books_authors.book_id = books.id \
        JOIN books_genres ON books.id = books_genres.book_id \
        JOIN genres ON books_genres.genre_id = genres.id \
        WHERE LOWER(authors.name) LIKE LOWER(%s)", (author,)
    )

    books_info = cursor.fetchall()
    cursor.close()

    return books_info
    

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    return render_template('main.html')

@app.route("/search", methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
    else:
        search_words = request.args['search_words']
        radio_button = request.args['radio_button']

    if radio_button == 'book':
        books_info = search_by_book(search_words)
    elif radio_button == 'author':
        books_info = search_by_author(search_words)

    return render_template('catalog.html', books_info=books_info)

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    return render_template('contact.html')

@app.route("/fantasy", methods=['GET', 'POST'])
def fantasy_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'Fantasy'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/novels", methods=['GET', 'POST'])
def novel_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'Novels'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/tales", methods=['GET', 'POST'])
def tale_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'Fairy tales'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/math", methods=['GET', 'POST'])
def math_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'Math'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/it", methods=['GET', 'POST'])
def it_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'IT'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/web", methods=['GET', 'POST'])
def web_page():
    if request.method == 'POST':
        search_words = request.form['search']
        radio_button = request.form['options']
        return redirect(url_for('search_page', search_words=search_words,
                                radio_button=radio_button))

    genre = 'Web'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
