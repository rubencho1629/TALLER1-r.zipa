from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'mi_secreto')

# Configuración de la base de datos
USER_DB = os.getenv('USER_DB')
PASS_DB = os.getenv('PASS_DB')
URL_DB = os.getenv('URL_DB')
NAME_DB = os.getenv('NAME_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirige a /login si no está autenticado

from .models.usuario import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Importar controladores
from .controllers.controllers import *  # Importa las rutas de controllers.py
from .controllers.user_controllers import *  # Importa las rutas de user_controllers.py
