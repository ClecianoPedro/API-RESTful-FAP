import json
import os

class JsonFileManager:

    @staticmethod
    def load_data(file_path: str) -> list:
        """Lê dados de um JSON. Caso o arquivo não exista, lança um erro."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON não encontrado: {file_path}")
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Erro ao ler o JSON: {file_path}")

    @staticmethod
    def save_data(file_path: str, data: list):
        """Salva uma lista de objetos em formato JSON."""
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
