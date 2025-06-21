from flask import Blueprint, jsonify

welcome_bp = Blueprint('welcome', __name__)

@welcome_bp.route('', methods=['GET'])
def saudacao():
    message = {'message': 'Bem-vindo à API de exemplo'}
    return jsonify(message), 200