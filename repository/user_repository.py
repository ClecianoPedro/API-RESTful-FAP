from model.user import User
from utils.load_user_data import save_users_to_file
from data.users import registered_users

class UserRepository:

    @staticmethod
    def save_user(data:object):
        registered_users.append(data)
        save_users_to_file()
        return data

    @staticmethod
    def get_user_by_id(id:int) -> object:
        for user in registered_users:
            if user.id == id:
                return user
            
    @staticmethod
    def get_user_by_email(new_email:str) -> bool:
        for user in registered_users:
            if user.email == new_email:
                return True
            return False

    @staticmethod
    def get_all_users() -> list:
        return registered_users

    @staticmethod
    def update_user(data: object) -> object:
        for index, user in enumerate(registered_users):
            if user.id == data.id:
                registered_users[index] = data
                save_users_to_file()
                return data

    @staticmethod
    def delete_user(id:int) -> bool:
        for i in registered_users:
            if i.id == id:
                registered_users.remove(i)
                save_users_to_file()
                return True
