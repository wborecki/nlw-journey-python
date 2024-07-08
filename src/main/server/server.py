from flask import Flask
from src.main.routes.trips_routes import trips_routes_bp

app = Flask(__name__)
