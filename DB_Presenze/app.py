from flask import Flask, render_template, request, redirect 
from urllib.parse import quote as url_quote
from datetime import datetime

app = Flask(__name__)
presenze = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        presenze.append({'nome': nome, 'data': data})
        return redirect(url_quote('index'))
    return render_template('index.html', presenze=presenze)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000, debug=True)
