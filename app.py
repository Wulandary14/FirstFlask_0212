from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Menampilkan halaman form awal
@app.route('/')
def index():
    return render_template('index.html', nama=None)

# Route 2: Khusus menerima data POST (tanpa GET)
@app.route('/kirim', methods=['POST'])
def kirim():
    nama = request.form['nama']
    return render_template('index.html', nama=nama)

if __name__ == '__main__':
    app.run(debug=True)