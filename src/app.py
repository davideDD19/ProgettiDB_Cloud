from flask import Flask, render_template, request

app = Flask(__name__)

nomi = []
nomi_ord = []

@app.route('/', methods=['GET', 'POST'])
def index():
 global nomi, nomi_ord
 if request.method == 'POST':
        if 'reset' in request.form:
            nomi.clear()
            nomi_ord.clear()
        elif 'nome' in request.form:
            nome = request.form["nome"]
            nomi.append(nome)
        elif 'ordina' in request.form:
            nomi_ord = sorted(nomi)
 return render_template('index.html', nomi=nomi, nomi_ord=nomi_ord)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
