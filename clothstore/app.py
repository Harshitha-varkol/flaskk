from flask import Flask
from config import Config
from extensions.db import db

from routes.mens_routes import mens_bp
from routes.womens_routes import womens_bp
from routes.kids_routes import kids_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(mens_bp)
app.register_blueprint(womens_bp)
app.register_blueprint(kids_bp)

if __name__ == "__main__":
    app.run(debug=True)
