import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://becqpvumueucmx:e9f98c48888d83d4c357055439bc511da13b10a8be21e991802e8f7f126c6a46@ec2-34-200-119-220.compute-1.amazonaws.com:5432/dcvgba94ar45id' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://becqpvumueucmx:e9f98c48888d83d4c357055439bc511da13b10a8be21e991802e8f7f126c6a46@ec2-34-200-119-220.compute-1.amazonaws.com:5432/dcvgba94ar45id'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)