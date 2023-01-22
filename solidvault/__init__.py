from flask import Flask, render_template, redirect, url_for, flash
from flask import request
import random, string

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def generate_password():  # put application's code here
    return render_template('generate.html', password="Your password here")


@app.route('/generate', methods=("GET", "POST"))
def generate():
    password = "Your password here"
    error = None
    if request.method == "POST":
        if request.args:
            post_args = request.args

            length = int(post_args["length-field"])
            word = post_args["word"]
            if (len(word) > length):
                error = "Word cannot be longer than the password length"
            has_lowercase = post_args["has_lowercase"] != "false"
            has_uppercase = post_args["has_uppercase"] != "false"
            has_digits = post_args["has_digits"] != "false"
            has_specials = post_args["has_specials"] != "false"
        else:
            length = int(request.form.get('length-field'))
            word = request.form.get('word')
            if (len(word) > length):
                error = "Word cannot be longer than the password length"
            has_lowercase = request.form.get('has_lowercase')
            has_uppercase = request.form.get('has_uppercase')
            has_digits = request.form.get('has_digits')
            has_specials = request.form.get('has_specials')

        if not (has_lowercase or has_uppercase or has_digits or has_specials):
            error = "At least one type of character must be selected"
            # return render_template("generate.html", password="Select at least one set of character")

        if error is not None:
            flash(error)
            return render_template("generate.html", password=password)
            # return redirect(url_for(filename="generate.html"), password=password)
        character_set = ""

        character_set += string.ascii_lowercase if has_lowercase else ""
        character_set += string.ascii_uppercase if has_uppercase else ""
        character_set += string.digits if has_digits else ""
        character_set += string.punctuation if has_specials else ""

        start = random.randint(0, length - len(word))
        password = ''.join(random.choice(character_set) for _ in range(start)).replace(' ', '')
        password += word
        password += ''.join(random.choice(character_set) for _ in range(length - (start+len(word)))).replace(' ', '')
        # print("lol")
        print(f"{length} letter(s) password : {password}")
    elif request.method == "GET":
        raise Exception
    return render_template("generate.html", password=password)


if __name__ == '__main__':
    app.run()
