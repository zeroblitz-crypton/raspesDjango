from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'products.db'
def create_db():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    codigo_raspe TEXT NOT NULL,
    codigo_lote TEXT NOT NULL,
    precio REAL NOT NULL
    );""")
    conn.commit()
    conn.close()
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    nombre = data['nombre']
    codigo_raspe = data['codigo_raspe']
    codigo_lote = data['codigo_lote']
    precio = data['precio']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (nombre, codigo_raspe, codigo_lote, precio) VALUES (?, ?, ?, ?)',
                   (nombre, codigo_raspe, codigo_lote, precio))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    result = [{'id': product['id'], 'nombre': product['nombre'], 'codigo_raspe': product['codigo_raspe'],
               'codigo_lote': product['codigo_lote'], 'precio': product['precio']} for product in products]
    return jsonify(result), 200

@app.route('/products/<int:product_id>', methods=['PUT'])

def update_product(product_id):
    data = request.get_json()
    nombre = data['nombre']
    codigo_raspe = data['codigo_raspe']
    codigo_lote = data['codigo_lote']
    precio = data['precio']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET nombre = ?, codigo_raspe = ?, codigo_lote = ?, precio = ? WHERE id = ?',
                   (nombre, codigo_raspe, codigo_lote, precio, product_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product updated successfully'}), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    create_db()
    app.run(debug=True)