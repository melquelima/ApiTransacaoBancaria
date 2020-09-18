from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
import os

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

from app.controllers import api
from app.controllers.API.V1.routes import *
from app.controllers.API.V2.routes import *


