from flask import Flask, request, jsonify

app = Flask(__name__)

greetings = {"default": "Hello, World!"}

@app.route('/api/hello', methods=['GET'])
def hello_api():
    return jsonify(message=greetings["default"])

@app.route('/api/greet', methods=['POST'])
def greet_api():
    data = request.get_json()
    name = data.get('name')
    if name:
        greetings["default"] = f"Hello, {name}!"
        return jsonify(message=greetings["default"])
    else:
        return jsonify(error="Name not provided"), 400

@app.route('/api/greet', methods=['PUT'])
def update_greet_api():
    data = request.get_json()
    name = data.get('name')
    if name:
        greetings["default"] = f"Updated greeting: Hello, {name}!"
        return jsonify(message=greetings["default"])
    else:
        return jsonify(error="Name not provided"), 400

@app.route('/api/greet', methods=['DELETE'])
def delete_greet_api():
    greetings["default"] = "Hello, World!"
    return jsonify(message="Greeting reset to default")

if __name__ == "__main__":
    app.run(debug=True)
