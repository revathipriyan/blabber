from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from .config import Config
from flask_socketio import SocketIO


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
app.config.from_object('app.config.Config')
db = SQLAlchemy(app)
socketio = SocketIO(app)

try:
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print("Database connection successful")
except OperationalError as e:
    print("Database connection failed:", e)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.endpoints.api import user


