import sqlite3
from flask import Flask, request, redirect, render_template_string
import string
import random

app = Flask(__name__)

# Database setup
def get_db():
    db = sqlite3.connect('urls.db')
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_code TEXT)')
        db.close()

init_db()

# Helper function to generate a random short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url
        
        short_code = generate_short_code()
        
        db = get_db()
        db.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
        db.commit()
        db.close()
        
        short_url = request.host_url + short_code
        return render_template_string('''
            <h1>URL Shortener</h1>
            <p>Shortened URL: <a href="{{ short_url }}">{{ short_url }}</a></p>
            <p><a href="{{ url_for('home') }}">Shorten another URL</a></p>
        ''', short_url=short_url)
    
    return render_template_string('''
        <h1>URL Shortener</h1>
        <form method="post">
            <input type="url" name="url" placeholder="Enter URL" required>
            <input type="submit" value="Shorten">
        </form>
    ''')

# Route for redirecting short URLs
@app.route('/<short_code>')
def redirect_to_url(short_code):
    db = get_db()
    result = db.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,)).fetchone()
    db.close()
    
    if result:
        return redirect(result['original_url'])
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)