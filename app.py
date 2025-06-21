from flask import Flask

from controller.welcome_controller import welcome_bp
from controller.user_controller import user_bp

app = Flask(__name__)

app.register_blueprint(welcome_bp, url_prefix='/saudacao')
app.register_blueprint(user_bp, url_prefix='/usuarios')

if __name__ == "__main__":
    app.run(debug=True)