from flask import Flask, render_template
from flask import request
import random, string, jinja2

app = Flask(__name__)


@app.route('/')
def generate_password():  # put application's code here
    return render_template('generate.html', password="Your password here")


@app.route('/generate', methods=("GET", "POST"))
def generate():
    password = "Your password here"
    if request.method == "POST":
        post_args = request.args
        print(post_args)

        length = int(post_args['length-field'])
        has_lowercase = post_args["has_lowercase"] != "false"
        has_uppercase = post_args["has_uppercase"] != "false"
        has_digits = post_args["has_digits"] != "false"
        has_specials = post_args["has_specials"] != "false"

        character_set = ""

        character_set += string.ascii_lowercase if has_lowercase else ""
        character_set += string.ascii_uppercase if has_uppercase else ""
        character_set += string.digits if has_digits else ""
        character_set += string.punctuation if has_specials else ""

        password = ''.join(random.choice(character_set) for _ in range(length)).replace(' ', '')
        print("lol")
        print(password)
    elif request.method == "GET":
        raise Exception
    return render_template("generate.html", password=password)


if __name__ == '__main__':
    app.run()
