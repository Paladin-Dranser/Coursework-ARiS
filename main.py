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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
