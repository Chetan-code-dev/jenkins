from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Do something with the form data, like sending an email or saving to a database
    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
