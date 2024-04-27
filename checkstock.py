from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # Change this to your MySQL host
app.config['MYSQL_DATABASE_USER'] = 'username'   # Change this to your MySQL username
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'  # Change this to your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'stock_database'  # Change this to your MySQL database name

mysql = MySQL(app)

@app.route('/check_stock', methods=['POST'])
def check_stock():
    try:
        # Get product name from the request
        product_name = request.json['product_name']

        # Query the database for the stock of the given product
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT stock FROM products WHERE name = %s", (product_name,))
        result = cursor.fetchone()

        if result:
            stock = result[0]
            return jsonify({"stock": stock})
        else:
            return jsonify({"error": "Product not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
