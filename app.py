from flask import Flask
from flask import render_template
app = Flask (__name__)

@app.route('/')
@app.route('/<nama>')
def index(nama = None):
    return render_template('index.html', user = nama)

@app.route('/undangandigital/')
def undangan():
    return render_template('Undangan.html')

if __name__ == '__main__':
    app.run()