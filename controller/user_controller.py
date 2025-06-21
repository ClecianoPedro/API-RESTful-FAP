from flask import Blueprint, request, jsonify
from service.user_service import UserService
from utils.functions import validate_email_with_domain, EmailNotValidError, format_string
from exceptions.UserExceptions import ExistingUserException, IdNotFoundException

user_bp = Blueprint('user', __name__)

@user_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    
    try:
        validate_email_with_domain(data['email'])
        email = data['email']
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

    try:
        name = format_string(data['name'], 'name')
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except AttributeError as ae:
        return jsonify({'Error': str(ae)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
    try:
        user_created = UserService.create_user(name, email)
        return jsonify(user_created.to_dict()), 201
    except ExistingUserException as eue:
        return jsonify({'Error':str(eue)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
@user_bp.route('/<int:id>', methods=['GET'])
def get_user_by_id(id):
    try:
        user = UserService.get_user_by_id(id)
        return jsonify(user.to_dict()), 200
    except IdNotFoundException as infe:
        return jsonify({'Error': str(infe)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

