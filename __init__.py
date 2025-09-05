from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap


#Initializing news_highlight
app = Flask(__name__, instance_relative_config=True, template_folder='app/models/__pychace__/templates', static_folder='app/models/__pychace__/static')

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask extensions
bootstrap = Bootstrap(app)


from views import *
from error import *