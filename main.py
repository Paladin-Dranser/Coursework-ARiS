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


def search(book_name):
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
    

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    return render_template('main.html')

@app.route("/search", methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        book_name = request.form['search']
    else:
        book_name = request.args['book_name']

    books_info = search(book_name)
    return render_template('catalog.html', books_info=books_info)

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    return render_template('contact.html')

@app.route("/fantasy", methods=['GET', 'POST'])
def fantasy_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'Fantasy'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/novels", methods=['GET', 'POST'])
def novel_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'Novels'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/tales", methods=['GET', 'POST'])
def tale_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'Fairy tales'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/math", methods=['GET', 'POST'])
def math_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'Math'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/it", methods=['GET', 'POST'])
def it_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'IT'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)

@app.route("/web", methods=['GET', 'POST'])
def web_page():
    if request.method == 'POST':
        book_name = request.form['search']
        return redirect(url_for('search_page', book_name=book_name))

    genre = 'Web'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', books_info=books_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
