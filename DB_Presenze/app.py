from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
presenze = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset' in request.form:
            presenze.clear()
        else:
            nome = request.form['nome']
            now = datetime.now().strftime("%H:%M:%S")  # Ottieni l'orario attuale
            if 'submit_entrata' in request.form:
                data_entrata = request.form['data_entrata']
                presenze.append({
                    'nome': nome,
                    'data_entrata': f"{data_entrata} {now}",  # Aggiungi l'orario alla data di entrata
                    'data_uscita': None
                })
            elif 'submit_uscita' in request.form:
                data_uscita = request.form['data_uscita']
                for presenza in presenze:
                    if presenza['nome'] == nome and presenza['data_uscita'] is None:
                        presenza['data_uscita'] = f"{data_uscita} {now}"  # Aggiungi l'orario alla data di uscita
                        break
        return redirect(url_for('index'))
    return render_template('index.html', presenze=presenze)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
