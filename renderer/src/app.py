from flask import Flask, jsonify, render_template
import random

# from main import db


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    pass
    # urls = list(db.get())
    # if len(urls):
    #     data = {'url': random.choices(urls)[0]['url']}
    #     return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0')
