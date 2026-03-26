from flask import Flask, render_template, request, redirect, url_for
from data_loader import load_data

app = Flask(__name__)
restaurants_data = load_data()

@app.route('/')
def index():

    all_restaurants = load_data()

    search_query = request.args.get('search', '').lower()
    sort_by = request.args.get('sort', '')
    min_rating = request.args.get('min_rating', type=float)

    # SEARCHING
    if search_query:
        restaurants = [
            r for r in all_restaurants 
            if search_query in r['name'].lower() 
            or search_query in r['cuisine'].lower()
        ]
    else:
        restaurants = all_restaurants

    # MIN RATING
    if min_rating:
        restaurants = [r for r in restaurants if r['rating'] >= min_rating]

    # SORTING
    if sort_by == 'rating_desc':
        restaurants = sorted(restaurants, key=lambda x: x['rating'], reverse=True)
    elif sort_by == 'rating_asc':
        restaurants = sorted(restaurants, key=lambda x: x['rating'])
    elif sort_by == 'time_asc':
        restaurants = sorted(restaurants, key=lambda x: x['delivery_time_mins'])
    elif sort_by == 'name_asc':
        restaurants = sorted(restaurants, key=lambda x: x['name'])
    elif sort_by == 'name_desc':
        restaurants = sorted(restaurants, key=lambda x: x['name'], reverse=True)

    total_found = len(restaurants)

    if total_found > 0:
        avg_delivery = sum(r['delivery_time_mins'] for r in restaurants) / total_found
    else:
        avg_delivery = 0

    return render_template(
        'index.html', 
        restaurants=restaurants, 
        total_count=total_found, 
        avg_time=round(avg_delivery)
    )

@app.route('/restaurant/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    restaurant = next((r for r in restaurants_data if r['id'] == restaurant_id), None)

    if not restaurant:
        if not restaurant:
            return "Restaurant not found", 404

    return render_template('restaurant_template.html', restaurant=restaurant)

if __name__ == '__main__':
    app.run(debug=True)