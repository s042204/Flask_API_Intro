from flask import Flask, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return f"App Config: {app.config['SECRET_KEY']}"

@app.route('/set_global')
def set_global():
    session['message'] = "Hello, this is a global variable!"
    return "Global variable set!"

@app.route('/get_global')
def get_global():
    message = session.get('message', "No global variable set!")
    return message

if __name__ == "__main__":
    with app.app_context():
        print(f"App Context: {app.config['SECRET_KEY']}")
    app.run(debug=True)
