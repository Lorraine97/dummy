# the main API application.

from flask import Flask
from .config import configure
from .blueprints.dummy_blueprint import blueprint
from .models import db_create
import pymysql

pymysql.install_as_MySQLdb()

#
# Create flask application and apply configuration
# http://flask.pocoo.org/docs/api/#application-object
# http://flask.pocoo.org/docs/config/
#

app = Flask(__name__, instance_relative_config=False)
app = configure(app)

# use SQLAlchemy in-built method to initiate the app db
db_create.init_app(app)
db_create.create_all(bind=None, app=app)

#
# Blueprint Registration
# Register blueprints
# http://flask.pocoo.org/docs/latest/blueprints/
#
app.register_blueprint(blueprint)

#
# def main():
#     app.run()
#
#
# if __name__ == '__main__':
#     main()
