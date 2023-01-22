from flask import Flask, render_template
from flask import request
import random
import string

app = Flask(__name__)

password = ""


@app.route('/')
def generate_password():  # put application's code here
    return render_template('generate.html')


@app.route('/generate', methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        length = request.form['length']
        has_lowercase = request.form['has_lowercase']
        has_uppercase = request.form['has_uppercase']
        has_digits = request.form['has_digits']
        has_special = request.form['has_special']

    character_set = ""

    character_set += string.ascii_lowercase if has_lowercase else ""
    character_set += string.ascii_uppercase if has_uppercase else ""
    character_set += string.digits if has_digits else ""
    character_set += string.punctuation if has_special else ""

    result = ''.join(random.choice(character_set) for _ in range(length)).replace(' ', '')
    return render_template("generate.html")x

if __name__ == '__main__':
    app.run()
