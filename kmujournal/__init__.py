from flask import Flask
app = Flask(__name__)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datastore
