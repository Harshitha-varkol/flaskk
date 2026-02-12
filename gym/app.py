from flask import Flask
from config import Config
from models.db import db
from flask_jwt_extended import JWTManager

from routes.auth_routes import auth_bp
from routes.trainer_routes import trainer_bp
from routes.gymrat_routes import gymrat_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(trainer_bp, url_prefix="/api")
app.register_blueprint(gymrat_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
