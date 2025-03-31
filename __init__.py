from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    # If you have any blueprints or additional configurations, add them here
    
    return app