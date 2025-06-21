from flask import Blueprint, jsonify

saudacao_bp = Blueprint('saudacao', __name__)

@saudacao_bp.route('', methods=['GET'])
def saudacao():
    message = {'message': 'Bem-vindo à API de exemplo'}
    return jsonify(message), 200