from flask import Flask
import pymysql.cursors

dummy_host = "localhost"
dummy_user = "dummy"
dummy_password = "dummy_pw"
dummy_db_name = "dummydatabase"

charSet = "utf8mb4"  # Character set

# Connect to the database
connection = pymysql.connect(host=dummy_host,
                             user='root',
                             charset=charSet,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # Create a cursor object
    cursorInsatnce = connection.cursor()
    # SQL Statement to create a database
    userStatement = f'CREATE USER IF NOT EXISTS {dummy_user}@{dummy_host} IDENTIFIED BY {dummy_password}'
    accessStatement = f'GRANT ALL PRIVILEGES ON *.* TO {dummy_user}@{dummy_host};'
    sqlStatement = f"CREATE DATABASE IF NOT EXISTS {dummy_db_name} "
    # Execute the create database SQL statment through the cursor instance
    cursorInsatnce.execute(userStatement)
    cursorInsatnce.execute(accessStatement)
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
    app.config.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dummy_user}:{dummy_password}@{dummy_host}/{dummy_db_name}'
    # app.config.from_object(Config)
    return app