from flask import Flask, abort, jsonify, request, json
from models import db, ma
from models.board import Board, BoardSchema
from api import test,board
import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(test.test_blueprint)
app.register_blueprint(board.board_blueprint)

@app.route('/', methods=['GET'])
def index():
    print()
    return '아아앙'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
