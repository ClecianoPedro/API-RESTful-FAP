from flask import Flask

from controller.saudacao_controller import saudacao_bp
from controller.user_controller import user_bp

app = Flask(__name__)

app.register_blueprint(saudacao_bp, url_prefix='/saudacao')
app.register_blueprint(user_bp, url_prefix='/usuarios')

if __name__ == "__main__":
    app.run(debug=True)