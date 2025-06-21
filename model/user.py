class User:
    def __init__(self, id:int, name:str, email:str, password:str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }