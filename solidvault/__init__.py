from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()



# from flask import Flask, send_from_directory
# import os
#
# from flask import (
#     Blueprint, render_template, current_app, g
# )
#
#
# def create_app():
#     app = Flask(__name__, instance_relative_config=True)
#
#     app.add_url_rule('/', 'index.html')
#
#     return app
