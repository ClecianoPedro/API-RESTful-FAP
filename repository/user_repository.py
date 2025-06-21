registered_users = []

class UserRepository:

    @staticmethod
    def save_user(data:object):
        registered_users.append(data)
        return data

    @staticmethod
    def get_user_by_id(id:int) -> object:
        for user in registered_users:
            if user.id == id:
                return user
