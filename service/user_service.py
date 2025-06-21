from model.user import User
from repository.user_repository import registered_users, UserRepository
from exceptions.UserExceptions import IdNotFoundException, ExistingUserException

class UserService:
    
    @staticmethod
    def create_user(name:str, email:str):
        for user in registered_users:
            if user.email == email:
                raise ExistingUserException('Email já cadastrado')
        id = len(registered_users) + 1
        try:
            return UserRepository.save_user(User(id, name, email))
        except Exception as e:
            raise e
        
    @staticmethod
    def get_user_by_id(id:int):
        user =  UserRepository.get_user_by_id(id)
        if user == None:
            raise IdNotFoundException('ID não encontrado')
        return user

