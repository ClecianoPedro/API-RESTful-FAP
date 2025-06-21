from flask import Blueprint, request, jsonify
from model.user import User
from service.user_service import UserService
from utils.functions import validate_email_with_domain, EmailNotValidError, format_string
from exceptions.UserExceptions import ExistingUserException

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
        user = User(name=format_string(data['name'], 'name'), email=email)
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except AttributeError as ae:
        return jsonify({'Error':str(ae)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
    try:
        user_created = UserService.create_user(user)
        return jsonify(user_created.to_dict()), 201
    except ExistingUserException as eue:
        return jsonify({'Error':str(eue)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404