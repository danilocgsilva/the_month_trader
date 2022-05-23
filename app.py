from flask import Flask

# Database handling
from flask_sqlalchemy import SQLAlchemy
# db must be instantiated very early, because some imports already will use
#   the instantiated db
db = SQLAlchemy()

# Authentication handling
from flask_login import LoginManager

# Routes
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes.symbol import symbol as symbol_blueprint

# Migrations
from flask_migrate import Migrate

# Middleware
from Middleware import Middleware

# Check environment variables, so is more secure set some information
#   as os environment variable rather than depends upon code
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('TMT_SECRET_KEY')


db_user = os.environ.get('TMT_DB_USER')
db_password = os.environ.get('TMT_DB_PASSWORD')
db_host = os.environ.get('TMT_DB_HOST')
db_database = os.environ.get('TMT_DB_DATABASE')
if os.environ.has_key('TMT_DB_PORT'):
    db_host += ":" + os.environ.get('TMT_DB_PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)

# Middlware utilization. REMEMBER: this code always must be used
#   before routes usage.
app.wsgi_app = Middleware(app.wsgi_app)

db.init_app(app)

from models import User

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(symbol_blueprint)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
