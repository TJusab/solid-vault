from flask import Flask, render_template
from flask import request
import random, string, jinja2

app = Flask(__name__)

realPassword = "Your password here"


@app.route('/')
def generate_password():  # put application's code here
    return render_template('generate.html', password=realPassword)


@app.route('/generate', methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        length = request.form['length-field']
        has_lowercase = request.form['has_lowercase']
        has_uppercase = request.form['has_uppercase']
        has_digits = request.form['has_digits']
        has_specials = request.form['has_specials']

        character_set = ""

        character_set += string.ascii_lowercase if has_lowercase else ""
        character_set += string.ascii_uppercase if has_uppercase else ""
        character_set += string.digits if has_digits else ""
        character_set += string.punctuation if has_specials else ""

        password = ''.join(random.choice(character_set) for _ in range(length)).replace(' ', '')
        print("lol")
        print(password)

    return render_template("generate.html", password=password)

if __name__ == '__main__':
    app.run()
