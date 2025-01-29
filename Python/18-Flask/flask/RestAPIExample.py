from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 100.00
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 200.00
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product) 

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201
    
# Update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((product for product in products if product['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    product['name'] = data['name']
    product['price'] = data['price']
    return jsonify(product)
    
# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    products.remove(product)
    return jsonify({'message': 'Product deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
    print('Server is running...')
    