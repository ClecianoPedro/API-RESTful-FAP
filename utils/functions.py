from string import punctuation
from email_validator import validate_email, EmailNotValidError
import re

def validate_email_with_domain(email:str):
    """Valida o email conforme RFC 5322 e verifica se o domínio possui registro DNS."""
    def validate_local_part(string: str) -> bool:
        partes = string.split('@', 1)
        if len(partes) < 2:
            return False
        return bool(re.fullmatch(r'[a-z0-9]+(\.[a-z0-9]+)*', partes[0]))
    
    if validate_local_part(email):
        try:
            if validate_email(email, check_deliverability=True):
                return True
        except EmailNotValidError as enve:
            raise ValueError(f"E-mail inválido: {str(enve)}")
        except Exception as e:
            # Captura erros como: falha de DNS
            raise ValueError(f"Erro ao validar o e-mail: {str(e)}")

def format_string(string:str, key:str):
    '''Remove os espaços do inicio e do final, caso haja 2 ou mais espaços seguidos substitui por apenas 1 e transforma 1 letra em maiúscula'''
    def replace_spaces(string):
        '''Substitui 2 ou mais espaços por apenas 1 e transforma para minusculo'''
        return re.sub(r'\s+', ' ', string).strip().capitalize()
    
    def has_special_characters(string:str) -> bool:
        '''Verifica se string contém caracteres especiais'''
        return any(char in punctuation for char in string)
    
    def contains_numbers(string: str) -> bool:
        '''Verifica se string contém digitos numéricos'''
        if any(char.isdigit() for char in string):
            return True
        return False
    
    if isinstance(string, str):
        if not string: #Verifica se string é vazia
            raise ValueError(f'{key} não pode ser vazia')
        elif string.isspace(): #Verifica se string contem somente espaços
            raise ValueError(f'{key} não pode conter somente espaços')
        elif contains_numbers(string):
            raise ValueError(f'{key} não pode conter números')
        elif has_special_characters(string):
            raise ValueError(f'{key} não pode conter caracteres especiais')
        string = replace_spaces(string)
        return string
    raise AttributeError(f'{key}: Valor deve ser do tipo string')
