from flask import Flask, render_template, request, redirect, url_for
from data_loader import load_data

app = Flask(__name__)
restaurants_data = load_data()

@app.route('/')
def index():

    all_restaurants = load_data()

    search_query = request.args.get('search', '').lower()
    sort_by = request.args.get('sort', '')

    if search_query:
        restaurants = [
            r for r in all_restaurants 
            if search_query in r['name'].lower() 
            or search_query in r['cuisine'].lower()
        ]
    else:
        restaurants = all_restaurants

    if sort_by == 'rating':
        restaurants = sorted(restaurants, key=lambda x: x['rating'], reverse=True)
    
    elif sort_by == 'time':
        restaurants = sorted(restaurants, key=lambda x: x['delivery_time_mins'])

    return render_template('index.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)