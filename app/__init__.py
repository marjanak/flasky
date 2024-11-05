from flask import Flask
from .routes.cat_routes import cats_bp
from.db import db, migrate
from .models import cat
import os
#from .models import caretaker

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.register_blueprint(cats_bp)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    if config:
        app.config.update(config)


    db.init_app(app)
    migrate.init_app(app,db)

    return app