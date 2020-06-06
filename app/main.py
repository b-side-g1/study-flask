from flask import Flask, abort, jsonify, request,json
from models import db,ma
from models.board import Board, BoardSchema

import config
import util
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    print()
    return '아아앙'

@app.route('/board', methods=['GET'])
def get_all_board():
    boards = Board.query.all()
    boardSchema = BoardSchema(many=True)

    output = boardSchema.dump(boards)

    return jsonify({
        'error': None,
        'payload': output
    })

@app.route('/post/<id>', methods=['GET'])
def get_board(id):
    post = Board.query.get(id)

    if not post:
        return abort(404)

    print('[main.py] #get_post post.id-> %s ' % post.id)
    print('[main.py] #get_post post.content-> %s ' % post.content)

    return jsonify({
        'id': post.id,
        'content': post.content
    })

@app.route('/board', methods=['POST'])
def add_board():
    body = request.get_json()
    print('[main.py] request body --> %s' % body)

    boardParam = {
        'id' : util.getUniqueId(),
        'writer': body['writer'],
        'content': body['content']
    }

    board = Board.query.filter_by(writer=boardParam['writer']).first()

    if board:
        return abort(400)

    insertParam = Board(boardParam['id'],boardParam['writer'],boardParam['content'])

    db.session.add(insertParam)
    db.session.commit()
    return jsonify({
        'error': None,
        'payload': boardParam
    })

@app.route('/board', methods=['PUT'])
def update_board():
    body = request.get_json()
    print('[main.py] request body --> %s' % body)

    boardParam = {
        'id': body['id'],
        'writer': body['writer'],
        'content': body['content']
    }

    board = Board.query.filter_by(id=boardParam['id']).first()
    print('[main.py] board --> %s' % board)

    if not board:
        return abort(400)

    board.writer = boardParam['writer']
    board.content = boardParam['content']

    db.session.commit()
    return jsonify({
        'error': None,
        'payload': boardParam
    })

@app.route('/board/<id>', methods=['DELETE'])
def delete_board(id):
    board = Board.query.filter_by(id=id).first()

    if not board:
        return abort(404)

    Board.query.filter_by(id=id).delete()
    db.session.commit()

    return jsonify({
        'id': id,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
