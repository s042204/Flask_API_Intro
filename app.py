from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')

@app.route('/<name>')
def print_name(name):
    return 'Hi , {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
