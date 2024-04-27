from flask import Flask, render_template, request, redirect, url_for
import mysql

app = Flask(__name__)

# MySQL Configuration
DB_HOST = 'localhost'
DB_USER = 'siddharth'
DB_PASSWORD = 'sidd@30'
DB_NAME = 'stock add'

# Function to establish a connection to MySQL
def get_db_connection():
    return mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Route to handle form submission
@app.route('/enroll', methods=['POST'])
def enroll():
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.form['productName']
        price = request.form['price']
        mfg = request.form['mfg']
        exp = request.form['exp']
        limiting_quantity = request.form['limitingQuantity']
        quantity = request.form['quantity']

        try:
            # Establish database connection
            conn = get_db_connection()
            cursor = conn.cursor()

            # SQL query to insert data into the database
            sql = "INSERT INTO stocks (product_name, price, mfg, exp, limiting_quantity, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (product_name, price, mfg, exp, limiting_quantity, quantity))
            
            # Commit changes and close connection
            conn.commit()
            cursor.close()
            conn.close()

            # Redirect to success page
            return redirect(url_for('enroll_success'))

        except Exception as e:
            # Print error message
            print("Error:", e)
            return "An error occurred while processing your request."

# Route for success page
@app.route('/enrollsuccess')
def enroll_success():
    return render_template('enrollsuccess.html')

if __name__ == '__main__':
    app.run(debug=True)
