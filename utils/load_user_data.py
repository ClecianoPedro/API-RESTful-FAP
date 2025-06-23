from model.user import User
from utils.file_manager import JsonFileManager
from config import DATA_FILE
from data.users import registered_users

def load_users_from_file() -> list:
    try:
        users_data = JsonFileManager.load_data(DATA_FILE)
        registered_users.clear()
        for user_dict in users_data:
            user = User(user_dict['id'], user_dict['name'], user_dict['email'])
            registered_users.append(user)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print(e)

def save_users_to_file():
    JsonFileManager.save_data(DATA_FILE, [user.to_dict() for user in registered_users])
