from flask import Flask
from flask_jwt_extended import JWTManager
from extensions import db
from routes import employee_bp
from auth import auth_bp
from config import Config
from datetime import timedelta  # <-- import timedelta

app = Flask(__name__)
app.config.from_object(Config)

# Set JWT token expiration to 24 hours
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(employee_bp)
app.register_blueprint(auth_bp)

# Create tables at startup
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
