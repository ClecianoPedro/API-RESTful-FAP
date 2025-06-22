from model.user import User
from repository.user_repository import registered_users, UserRepository
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
    def update_user(id:int, name:str, email:str) -> object:
        user = UserService.get_user_by_id(id)
        if UserService.get_user_by_email(email):
            raise EmailException ('Endereço de email já está em uso')
        user.name = name
        user.email = email
        
        user_updated = UserRepository.update_user(user)
        if user_updated:
            return user_updated
