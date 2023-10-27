from flask import Flask, jsonify, render_template
import os
import random

from main import db


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    urls = list(db.get())
    if len(urls):
        data = {'url': random.choices(urls)[0]['url']}
        return jsonify(data)
    else:
        return jsonify({'url': 'https://images.metmuseum.org/CRDImages/ad/web-large/ap66.142.jpg'})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)
