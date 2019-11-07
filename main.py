from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('main.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/fantasy")
def fantasy_page():
    genre = 'Fantasy'
    return render_template('catalog.html', genre=genre)

@app.route("/novels")
def novel_page():
    genre = 'Novel'
    return render_template('catalog.html', genre=genre)

@app.route("/tales")
def tale_page():
    genre = 'Tale'
    return render_template('catalog.html', genre=genre)

@app.route("/math")
def math_page():
    genre = 'Math'
    return render_template('catalog.html', genre=genre)

@app.route("/it")
def it_page():
    genre = 'IT'
    return render_template('catalog.html', genre=genre)

@app.route("/web")
def web_page():
    genre = 'Web'
    return render_template('catalog.html', genre=genre)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
