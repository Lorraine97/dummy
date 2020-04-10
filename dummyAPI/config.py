from flask import Flask
import pymysql.cursors

dummy_host = "localhost"
dummy_user = "dummy"
dummy_password = "dummy_pw"
dummy_db_name = "dummydatabase"

charSet = "utf8mb4"  # Character set

# Connect to the database
connection = pymysql.connect(host=dummy_host,
                             user=dummy_user,
                             password=dummy_password,
                             charset=charSet,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # Create a cursor object
    cursorInsatnce = connection.cursor()
    # SQL Statement to create a database
    sqlStatement = f"CREATE DATABASE IF NOT EXISTS {dummy_db_name} "
    accessStatement = f'GRANT ALL PRIVILEGES ON database_name. * TO {dummy_user} @ {dummy_host};'
    # Execute the create database SQL statment through the cursor instance
    cursorInsatnce.execute(sqlStatement)
except Exception as e:
    print("Exception {}".format(e))
finally:
    connection.close()


class Config(object):
    DEBUG = False,  # Flask built-in debug mode
    TESTING = False,  # Flask built-in testing mode
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dummy_user}:{dummy_password}@{dummy_host}/{dummy_db_name}',
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def configure(app):
    app.config.from_object(Config)
    return app