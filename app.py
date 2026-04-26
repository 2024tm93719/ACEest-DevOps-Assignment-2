from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "fitness.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        weight REAL
    )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    conn.close()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET','POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("INSERT INTO clients (name, age, weight) VALUES (?, ?, ?)",
                    (name, age, weight))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_client.html')

init_db()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)