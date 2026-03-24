from flask import Flask, render_template, request, redirect, url_for
from data_loader import load_data

app = Flask(__name__)
restaurants_data = load_data()

@app.route('/')
def index():

    restaurants = load_data()

    return render_template('index.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)