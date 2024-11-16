from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

app = Flask(__name__)

# In-memory storage for demo (can be replaced with a database)
products = [
    {"id": 1, "name": "MacBook Pro", "price": 1200, "image_url": "product1.jpg"},
    {"id": 2, "name": "Dell XPS 13", "price": 900, "image_url": "product2.jpg"},
    {"id": 3, "name": "HP Spectre x360", "price": 1100, "image_url": "product3.jpg"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    image_url = request.form.get('image_url')

    # Add product to the list
    new_product = {
        "id": len(products) + 1,
        "name": name,
        "price": float(price),
        "image_url": image_url
    }
    products.append(new_product)

    return redirect(url_for('home'))

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
