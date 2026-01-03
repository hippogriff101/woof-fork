from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dogs')
def new_page():
    return render_template('dogs.html')

if __name__ == '__main__':
    app.run()