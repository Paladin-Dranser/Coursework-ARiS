from flask import Flask, render_template, url_for, request, redirect
import mysql.connector as mariadb


mariadb_connection = mariadb.connect(
    user='flask_user',
    password='password',
    database='flask_coursework'
)

def get_books_by_genre(genre):
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT books.name, books.pdf_link, books.image_link FROM genres \
        JOIN books_genres ON genres.id = books_genres.genre_id \
        JOIN books ON books_genres.book_id = books.id \
        WHERE genres.name = %s", (genre,)
    )

    books_info = cursor.fetchall()
    cursor.close()

    return books_info


def search(book_name):
    book_name = '%' + book_name + '%'
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT name, pdf_link, image_link FROM books \
        WHERE name LIKE %s", (book_name,)
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

@app.route("/search")
def search_page():
    book_name = request.args['book_name']
    books_info = search(book_name)
    return render_template('catalog.html', genre='', books_info=books_info)

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/fantasy")
def fantasy_page():
    genre = 'Fantasy'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)

@app.route("/novels")
def novel_page():
    genre = 'Novel'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)

@app.route("/tales")
def tale_page():
    genre = 'Tale'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)

@app.route("/math")
def math_page():
    genre = 'Math'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)

@app.route("/it")
def it_page():
    genre = 'IT'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)

@app.route("/web")
def web_page():
    genre = 'Web'
    books_info = get_books_by_genre(genre)
    return render_template('catalog.html', genre=genre, books_info=books_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
