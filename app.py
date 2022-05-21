from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from flask_migrate import Migrate
import os

db_user = os.environ.get('TMT_DB_USER')
db_password = os.environ.get('TMT_DB_PASSWORD')
db_host = os.environ.get('TMT_DB_HOST')
db_database = os.environ.get('TMT_DB_DATABASE')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)

db.init_app(app)

from models import User

app.register_blueprint(auth_blueprint)

app.register_blueprint(main_blueprint)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
