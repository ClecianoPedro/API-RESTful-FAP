from flask import Blueprint, request, jsonify
from service.user_service import UserService
from utils.functions import validate_email_with_domain, EmailNotValidError, format_string
from exceptions.UserExceptions import ExistingUserException, IdNotFoundException, EmailException

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

@user_bp.route('', methods=['GET'])
def get_all():
    try:
        users = UserService.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 404
    
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    try:
        UserService.get_user_by_id(id)
    except IdNotFoundException as infe:
        return jsonify({'Error': str(infe)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

    try:
        validate_email_with_domain(data['email'])
        new_email = data['email']
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
        user_updated = UserService.update_user(id, name, new_email)
        return jsonify(user_updated.to_dict()), 200
    except IdNotFoundException as infe:
        return jsonify({'Error': str(infe)}), 400
    except EmailException as ee:
        return jsonify({'Error': str(ee)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404

@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user_to_delete = UserService.delete_user(id)
        return jsonify({'Message': str(user_to_delete)}), 200
    except IdNotFoundException as idne:
        return jsonify({'Error': str(idne)}), 400
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404
