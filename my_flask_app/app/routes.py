from flask import Blueprint

views = Blueprint('views', 'app.views')  # Import your views Blueprint

def init_app(app):
    app.register_blueprint(views)
    
