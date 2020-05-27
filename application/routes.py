from flask_restful import Api
from application import resources


def create_route(app):
    api = Api(app)
    api.add_resource(resources.UserRegistration, '/registration')
    api.add_resource(resources.UserLogin, '/login')
    api.add_resource(resources.TokenRefresh, '/token/refresh')
    api.add_resource(resources.AllUsers, '/users')
    api.add_resource(resources.SecretResource, '/secret')
