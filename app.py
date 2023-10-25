from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)
url_database = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    if original_url not in url_database:
        short_url = generate_short_url()
        url_database[original_url] = short_url
    else:
        short_url = url_database[original_url]
    return render_template('shorten.html', original_url=original_url, short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    for original_url, stored_short_url in url_database.items():
        if stored_short_url == short_url:
            return redirect(original_url)
    return "URL not found."

if __name__ == '__main__':
    app.run()
