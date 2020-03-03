from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Athena',
        'index': True
    }
    return render_template('index.html', context=context)

@app.route('/lstHistorias')
def lstHistorias():
    context = {
        'title': 'Athena',
        'lstHistorias': True,
        'lista': ['nome1', 'nome2', 'nome3', 'nome4', 'nome final']
    }
    return render_template( 'lstHistorias.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
