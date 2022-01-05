from flask import Flask
from flask_script import Manager


app = Flask(__name__)


from home.controller import default