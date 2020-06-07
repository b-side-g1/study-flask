from flask import Blueprint, render_template

test_blueprint = Blueprint('TEST_ROUTER', __name__)

@test_blueprint.route("/test",methods=['POST'])
def index():
    return "Hello World!"