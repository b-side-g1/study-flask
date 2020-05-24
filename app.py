from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

userParser = reqparse.RequestParser()
userParser.add_argument('id', required=True, type=str, help='id cannot be blank')
userParser.add_argument('pwd', required=True, type=str, help='pwd cannot be blank')

DB_FILE = './database/users.json'


class UserList(Resource):

    def get(self):
        with open(DB_FILE, 'r') as f:
            json_data = json.load(f)
        return json_data

    def post(self):
        try:
            args = userParser.parse_args()
            print(args)
            id = args['id']
            pwd = args['pwd']

            user = dict()
            user['id'] = id
            user['pwd'] = pwd

            with open(DB_FILE, 'r') as f:
                json_data = json.load(f)
            json_data.append(user)

            with open(DB_FILE, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent="\t")
            return user, 200
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(UserList, '/users')

app.run(debug=True)
