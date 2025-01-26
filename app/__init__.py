from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from prometheus_flask_exporter import PrometheusMetrics

# Inicialización de la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

# Inicialización de la base de datos
db = SQLAlchemy(app)

# Inicialización del Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Inicialización de Prometheus Metrics para monitoreo
metrics = PrometheusMetrics(app)

from app import routes
