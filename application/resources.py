from flask_restful import Resource, reqparse
import json
from hashlib import sha256
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import pathlib
parser = reqparse.RequestParser()
parser.add_argument('username', required=True, type=str, help='This field cannot be blank')
parser.add_argument('password', required=True, type=str, help='This field cannot be blank')

DB_FILE = str(pathlib.Path().absolute())+'/database/users.json'


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        user = dict()
        user['username'] = data['username']
        user['password'] = data['password']

        with open(DB_FILE, 'r') as f:
            json_data = json.load(f)

        for user_data in json_data:
            if user_data['username'] == user['username']:
                return {'message': 'User {} already exists'. format(user['username'])}

        user['password'] = sha256(user['password'].encode('utf-8')).hexdigest()
        json_data.append(user)

        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent="\t")

        return user


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        print(data)
        with open(DB_FILE, 'r') as f:
            json_data = json.load(f)

        current_user = ''
        for user_data in json_data:
            if data['username'] == user_data['username']:
                current_user = user_data
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 400

        hashPassword = sha256(data['password'].encode('utf-8')).hexdigest()
        if current_user['password'] == hashPassword:
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {'message': 'Logged in as {}.'.format(current_user['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token}, 200
        else:
            return {'message': 'Wrong credentials.'}, 400


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        with open(DB_FILE, 'r') as f:
            json_data = json.load(f)
        return json_data


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }

