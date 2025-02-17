import os
from flask import Response, Flask, flash, render_template, request, redirect, url_for, session, jsonify, Response
from flask_mysqldb import MySQL
import mysql.connector
import subprocess
from mysql.connector import Error
from datetime import date, datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, exists, and_
import logging
from my_flask_app.config import Config


logging.basicConfig(level=logging.DEBUG)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/SysAd'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'pooKey'
    
    # Initialize db with app
    db.init_app(app)
    
    # Import and register blueprints
    from .app import routes
    from .app.views import views
    app.register_blueprint(views)
    
    return app
