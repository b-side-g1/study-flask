from flask import Blueprint, jsonify, abort, request
from models import db
from models.board import Board, BoardSchema
import util

board_blueprint = Blueprint('BOARD_ROUTER', __name__)


@board_blueprint.route('/board', methods=['GET'])
def get_all_board():
    boards = Board.query.all()
    boardSchema = BoardSchema(many=True)

    output = boardSchema.dump(boards)

    return jsonify({
        'error': None,
        'payload': output
    }), 200


@board_blueprint.route('/board/<id>', methods=['GET'])
def get_board(id):
    board = Board.query.get(id)

    if not board:
        return abort(404)

    return jsonify({
        'id': board.id,
        'content': board.content
    }), 200

@board_blueprint.route('/board', methods=['POST'])
def add_board():
    body = request.get_json()
    print('[main.py] request body --> %s' % body)

    boardParam = {
        'id': util.getUniqueId(),
        'writer': body['writer'],
        'content': body['content']
    }

    board = Board.query.filter_by(writer=boardParam['writer']).first()

    if board:
        return abort(400)

    insertParam = Board(boardParam['id'], boardParam['writer'], boardParam['content'])

    db.session.add(insertParam)
    db.session.commit()
    return jsonify({
        'error': None,
        'payload': boardParam
    }), 200

@board_blueprint.route('/board', methods=['PUT'])
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
    }), 200

@board_blueprint.route('/board/<id>', methods=['DELETE'])
def delete_board(id):
    board = Board.query.filter_by(id=id).first()

    if not board:
        return abort(404)

    Board.query.filter_by(id=id).delete()
    db.session.commit()

    return jsonify({
        'id': id,
    }), 200