class ExistingUserException(Exception):
    def __init__(self, message):
        super().__init__(message)

class IdNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class EmailException(Exception):
    def __init__(self, message):
        super().__init__(message)