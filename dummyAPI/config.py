class Config(object):
    DEBUG = False  # Flask built-in debug mode
    TESTING = False  # Flask built-in testing mode
    # ------- local
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' \
                              'dummy:dummy_pw' \
                              '@localhost/dummydatabase'
    # ------- personal aws
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' \
    #                           'dummy:dummy_pw' \
    #                           '@dummydatabase.czezhntz7jjw.us-east-2.rds.amazonaws.com/dummydatabase'
    # ------- dtn aws
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' \
    #                           'admin:GfswGK3ZbQrAaI8s5trK' \
    #                           '@xinru-dummydatabase.c2syjj4dqthv.us-east-1.rds.amazonaws.com/dummydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def configure(app):
    app.config.from_object(Config)
    return app


# admin
# GfswGK3ZbQrAaI8s5trK
#
# xinru-dummydatabase.c2syjj4dqthv.us-east-1.rds.amazonaws.com


#
#     userStatement = f"CREATE USER IF NOT EXISTS '{dummy_user}'@'{dummy_host}' IDENTIFIED BY '{dummy_password}';"
#     accessStatement = f"GRANT ALL PRIVILEGES ON {dummy_db_name}.* TO '{dummy_user}'@'{dummy_host}';"
