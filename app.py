from flask import Flask, render_template
app = Flask(__name__)

flashcards = [
    {'id': 1, 'term': 'Apple', 'definition': 'Яблоко'},
    {'id': 2, 'term': 'Book', 'definition': 'Книга'},
    {'id': 3, 'term': 'House', 'definition': 'Дом'}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html', flashcards=flashcards)


if __name__ == '__main__':
    app.run(debug=True)