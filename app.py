from flask import Flask, jsonify, request
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/getuser', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Persons')
    rows = cursor.fetchall()
    
    data = []
    for row in rows:
        data.append({
            'Id': row[4],
            'First_Name': row[0]
        })
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
