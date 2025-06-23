from model.user import User
from data.users import registered_users
from repository.user_repository import UserRepository

from exceptions.UserExceptions import IdNotFoundException, ExistingUserException, EmailException

class UserService:
    
    @staticmethod
    def create_user(name:str, email:str) -> object:
        for user in registered_users:
            if user.email == email:
                raise ExistingUserException('Email já cadastrado')
        id = len(registered_users) + 1
        try:
            return UserRepository.save_user(User(id, name, email))
        except Exception as e:
            raise e
        
    @staticmethod
    def get_user_by_id(id:int) -> object:
        user =  UserRepository.get_user_by_id(id)
        if user == None:
            raise IdNotFoundException('ID não encontrado')
        return user

    @staticmethod
    def get_user_by_email(email:str) -> bool:
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def get_all_users() -> list:
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]
    
    @staticmethod
    def update_user(id:int, name:str, new_email:str) -> object:
        user = UserService.get_user_by_id(id)
        for i in registered_users:
            if i.email == new_email and i.id != id:
                raise EmailException('Email já está em uso')
            user.name = name
            user.email = new_email
        
        return UserRepository.update_user(user)

    @staticmethod
    def delete_user(id:int) -> object:
        if UserService.get_user_by_id(id):
            return UserRepository.delete_user(id)
