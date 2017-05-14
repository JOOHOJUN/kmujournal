from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


db.create_all()
