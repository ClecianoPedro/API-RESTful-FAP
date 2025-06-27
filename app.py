from flask import Flask
from controller.welcome_controller import welcome_bp
from controller.user_controller import user_bp
from utils.load_user_data import load_users_from_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    load_users_from_file()
    print('Usuários carregados com sucesso.')
except Exception as e:
    print(f'Falha ao carregar usuários: {e}')
    exit(1)

app.register_blueprint(welcome_bp, url_prefix='/saudacao')
app.register_blueprint(user_bp, url_prefix='/usuarios')

if __name__ == '__main__':
    import os
    try:
        port = int(os.environ.get("PORT", 5000))
    except ValueError:
        port = 5000
    app.run(host="0.0.0.0", port=port)
