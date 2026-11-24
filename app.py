from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}

    if request.method == 'POST':
        data['nama']=request.form['nama']
        data['umur']=request.form['umur']
        data['gender']=request.form['gender']

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)